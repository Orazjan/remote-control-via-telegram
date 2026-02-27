import asyncio
import logging
import os
import platform

import comtypes
import screen_brightness_control as sbc
from aiogram import F, Router, types
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from environs import Env
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

from Funcs import funcs, state

logger = logging.getLogger(__name__)

# Инициализация переменных окружения и роутера
env = Env()
env.read_env()
ADMIN_ID = env.int('id')

# Создаем роутер прямо здесь, чтобы управлять всем из одного места
router = Router()

# Класс для callback-данных звука


class AudioCallback(CallbackData, prefix="Звук"):
    action: str
    name: str


class StatusCommands:
    @staticmethod
    def setup_logging():
        """Настраивает запись логов в файл отдельно от консоли"""
        log_path = f"{funcs.PATH}logfile.log"

        file_formatter = logging.Formatter(
            "%(levelname)s %(asctime)s - %(message)s")
        file_handler = logging.FileHandler(
            log_path, mode="w", encoding='utf-8')
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.ERROR)

        root_logger = logging.getLogger()
        root_logger.addHandler(file_handler)

        proc_info = platform.processor()
        root_logger.info(state.return_message(
            f"Log file initialized. Processor: {proc_info}"))

    @staticmethod
    async def kill_process(process_name: str):
        """Убивает процесс по имени"""
        await asyncio.to_thread(os.system, f"taskkill /f /im {process_name}")

    @staticmethod
    async def get_brightness():
        """Получает яркость мониторов"""
        try:
            monitors = await asyncio.to_thread(sbc.list_monitors)
            if not monitors:
                return "Мониторы не найдены или не поддерживают управление."

            result = ""
            for monitor in monitors:
                b_level = await asyncio.to_thread(sbc.get_brightness, display=monitor)
                val = b_level[0] if isinstance(b_level, list) else b_level
                result += f"Монитор: {monitor}\nЯркость: {val}%\n"
            return result
        except Exception as e:
            logger.error(f"Ошибка получения яркости: {e}")
            return "Не удалось получить данные о яркости."

    @staticmethod
    async def bright_monitor(percent):
        """Устанавливает яркость"""
        try:
            await asyncio.to_thread(sbc.set_brightness, int(percent))
        except Exception as e:
            logger.error(f"Ошибка установки яркости: {e}")

    @staticmethod
    async def get_audio_sessions():
        """Получает список всех приложений, которые сейчас используют звук."""
        def _get_sessions_sync():
            comtypes.CoInitialize()
            try:
                sessions_list = []
                sessions = AudioUtilities.GetAllSessions()
                for session in sessions:
                    volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                    if session.Process:
                        name = session.Process.name()
                        current_vol = volume.GetMasterVolume()
                        is_muted = volume.GetMute()

                        sessions_list.append({
                            "name": name,
                            "volume": round(current_vol * 100),
                            "is_muted": is_muted
                        })
                return sessions_list
            finally:
                comtypes.CoUninitialize()

        return await asyncio.to_thread(_get_sessions_sync)

    @staticmethod
    async def set_app_volume(app_name: str, change: int):
        """Изменяет громкость приложения."""
        def _set_vol_sync():
            comtypes.CoInitialize()
            try:
                sessions = AudioUtilities.GetAllSessions()
                for session in sessions:
                    if session.Process and session.Process.name() == app_name:
                        volume = session._ctl.QueryInterface(
                            ISimpleAudioVolume)
                        current = volume.GetMasterVolume()
                        new_vol = min(1.0, max(0.0, current + (change / 100)))
                        volume.SetMasterVolume(new_vol, None)
                        return True
                return False
            finally:
                comtypes.CoUninitialize()

        return await asyncio.to_thread(_set_vol_sync)

    @staticmethod
    async def toggle_mute(app_name: str):
        """Включает/выключает звук у приложения"""
        def _mute_sync():
            comtypes.CoInitialize()
            try:
                sessions = AudioUtilities.GetAllSessions()
                for session in sessions:
                    if session.Process and session.Process.name() == app_name:
                        volume = session._ctl.QueryInterface(
                            ISimpleAudioVolume)
                        current_mute = volume.GetMute()
                        volume.SetMute(not current_mute, None)
                        return True
                return False
            finally:
                comtypes.CoUninitialize()

        return await asyncio.to_thread(_mute_sync)


@router.message(Command("Звук"), F.from_user.id == ADMIN_ID)
async def cmd_mixer(message: types.Message):
    await send_mixer_menu(message)


async def send_mixer_menu(message_or_call):
    sessions = await StatusCommands.get_audio_sessions()
    builder = InlineKeyboardBuilder()

    if not sessions:
        text = "Нет активных звуковых приложений."
        if isinstance(message_or_call, types.CallbackQuery):
            try:
                await message_or_call.message.edit_text(text)
            except TelegramBadRequest:
                await message_or_call.answer(text)
        else:
            await message_or_call.answer(text)
        return

    for app in sessions:
        status = "🔇" if app['is_muted'] else "🔊"
        btn_text = f"{status} {app['name']} [{app['volume']}%]"
        builder.button(
            text=btn_text,
            callback_data=AudioCallback(action="select", name=app['name'])
        )

    builder.adjust(1)
    builder.button(text="❌ Закрыть", callback_data=AudioCallback(
        action="close", name="none"))

    text = "🎚 <b>Аудио Микшер</b>\nВыберите приложение:"

    if isinstance(message_or_call, types.Message):
        await message_or_call.answer(text, reply_markup=builder.as_markup(), parse_mode="HTML")
    elif isinstance(message_or_call, types.CallbackQuery):
        try:
            await message_or_call.message.edit_text(text, reply_markup=builder.as_markup(), parse_mode="HTML")
        except TelegramBadRequest:
            pass


@router.callback_query(AudioCallback.filter(F.action == "select"))
async def process_app_select(call: CallbackQuery, callback_data: AudioCallback):
    app_name = callback_data.name
    await render_app_controls(call, app_name)


async def render_app_controls(call: CallbackQuery, app_name: str):
    sessions = await StatusCommands.get_audio_sessions()
    current_app_data = next(
        (s for s in sessions if s['name'] == app_name), None)

    if not current_app_data:
        await call.answer("Приложение уже закрыто.")
        await send_mixer_menu(call)
        return

    vol = current_app_data['volume']
    is_muted = current_app_data['is_muted']
    status_icon = "🔇" if is_muted else "🔊"

    builder = InlineKeyboardBuilder()
    builder.button(text="➖ 10%", callback_data=AudioCallback(
        action="v_down", name=app_name))
    builder.button(text="🔇/🔊 Mute",
                   callback_data=AudioCallback(action="mute", name=app_name))
    builder.button(text="➕ 10%", callback_data=AudioCallback(
        action="v_up", name=app_name))
    builder.button(text="🔙 Назад", callback_data=AudioCallback(
        action="back", name="none"))

    builder.adjust(3, 1)

    text = f"Настройка: <b>{app_name}</b>\nГромкость: {vol}% {status_icon}"

    try:
        await call.message.edit_text(text, reply_markup=builder.as_markup(), parse_mode="HTML")
    except TelegramBadRequest:
        pass


@router.callback_query(AudioCallback.filter(F.action.in_({"v_up", "v_down", "mute"})))
async def process_volume_change(call: CallbackQuery, callback_data: AudioCallback):
    action = callback_data.action
    app_name = callback_data.name

    if action == "v_up":
        await StatusCommands.set_app_volume(app_name, 10)
    elif action == "v_down":
        await StatusCommands.set_app_volume(app_name, -10)
    elif action == "mute":
        await StatusCommands.toggle_mute(app_name)

    await render_app_controls(call, app_name)
    await call.answer(f"Выполнено: {action}")


@router.callback_query(AudioCallback.filter(F.action == "back"))
async def process_back(call: CallbackQuery):
    await send_mixer_menu(call)


@router.callback_query(AudioCallback.filter(F.action == "close"))
async def process_close(call: CallbackQuery):
    await call.message.delete()
    await call.answer()
