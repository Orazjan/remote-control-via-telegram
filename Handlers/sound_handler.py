from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram.exceptions import TelegramBadRequest
from environs import Env

from Funcs.sound_utils import SoundUtils

env = Env()
env.read_env()
ADMIN_ID = env.int('id')

router = Router()


class AudioCallback(CallbackData, prefix="zvuk"):
    action: str
    name: str


@router.message(Command("zvuk"), F.from_user.id == ADMIN_ID)
async def cmd_mixer(message: types.Message):
    await send_mixer_menu(message)

# --- Функция отправки главного меню ---


async def send_mixer_menu(message_or_call):
    # Получаем список программ
    sessions = await SoundUtils.get_audio_sessions()

    builder = InlineKeyboardBuilder()

    if not sessions:
        text = "Нет активных звуковых приложений."
        if isinstance(message_or_call, types.CallbackQuery):
            # Если список пуст, но мы пришли из меню, пробуем изменить текст
            try:
                await message_or_call.message.edit_text(text)
            except TelegramBadRequest:
                await message_or_call.answer(text)
        else:
            await message_or_call.answer(text)
        return

    # Генерируем кнопки для каждого приложения
    for app in sessions:
        status = "🔇" if app['is_muted'] else "🔊"
        btn_text = f"{status} {app['name']} [{app['volume']}%]"

        builder.button(
            text=btn_text,
            callback_data=AudioCallback(action="select", name=app['name'])
        )

    builder.adjust(1)

    # Кнопка закрытия
    builder.button(text="❌ Закрыть", callback_data=AudioCallback(
        action="close", name="none"))

    text = "🎚 <b>Аудио Микшер</b>\nВыберите приложение:"

    if isinstance(message_or_call, types.Message):
        await message_or_call.answer(text, reply_markup=builder.as_markup(), parse_mode="HTML")
    elif isinstance(message_or_call, types.CallbackQuery):
        # try-except нужен, чтобы не было ошибки, если текст не изменился
        try:
            await message_or_call.message.edit_text(text, reply_markup=builder.as_markup(), parse_mode="HTML")
        except TelegramBadRequest:
            pass

# --- Выбор конкретного приложения ---


@router.callback_query(AudioCallback.filter(F.action == "select"))
async def process_app_select(call: CallbackQuery, callback_data: AudioCallback):
    app_name = callback_data.name
    await render_app_controls(call, app_name)

# --- Функция отрисовки пульта управления ---


async def render_app_controls(call: CallbackQuery, app_name: str):
    """Рисует или обновляет меню управления конкретным приложением"""

    # Получаем актуальные данные, чтобы показать правильный % громкости
    sessions = await SoundUtils.get_audio_sessions()
    # Ищем наше приложение в списке
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
        # Если пользователь быстро жмет кнопки, текст может не успеть измениться, игнорируем ошибку
        pass

# --- Обработка кнопок изменения громкости ---


@router.callback_query(AudioCallback.filter(F.action.in_({"v_up", "v_down", "mute"})))
async def process_volume_change(call: CallbackQuery, callback_data: AudioCallback):
    action = callback_data.action
    app_name = callback_data.name

    if action == "v_up":
        await SoundUtils.set_app_volume(app_name, 10)
    elif action == "v_down":
        await SoundUtils.set_app_volume(app_name, -10)
    elif action == "mute":
        await SoundUtils.toggle_mute(app_name)

    await render_app_controls(call, app_name)
    await call.answer(f"Выполнено: {action}")


# --- Кнопка Назад ---
@router.callback_query(AudioCallback.filter(F.action == "back"))
async def process_back(call: CallbackQuery):
    await send_mixer_menu(call)

# --- Кнопка Закрыть ---


@router.callback_query(AudioCallback.filter(F.action == "close"))
async def process_close(call: CallbackQuery):
    await call.message.delete()
    await call.answer()
