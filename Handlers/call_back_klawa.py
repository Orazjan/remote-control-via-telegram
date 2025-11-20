import asyncio

import pyautogui as pag
from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from environs import Env

# 1. Настройка переменных
env = Env()
env.read_env()
ADMIN_ID = env.int('id')

router = Router()

# 2. Новая система CallbackData (в стиле V3)
# Мы создаем класс, описывающий данные кнопки


class VoteCallback(CallbackData, prefix="vote"):
    action: str
    amount: int

# 3. Создание клавиатуры через Builder (современный способ)


def get_keyboard(amount: int):
    builder = InlineKeyboardBuilder()

    # Добавляем кнопки. Обрати внимание на создание callback_data
    builder.button(text='⬆️ Up', callback_data=VoteCallback(
        action='up', amount=amount))
    builder.button(text='⬅️ Left', callback_data=VoteCallback(
        action='left', amount=amount))
    builder.button(text='➡️ Right', callback_data=VoteCallback(
        action='right', amount=amount))
    builder.button(text='⬇️ Down', callback_data=VoteCallback(
        action='down', amount=amount))
    builder.button(text='⏯ Play/Pause',
                   callback_data=VoteCallback(action='pause', amount=amount))
    builder.button(text='❌ End', callback_data=VoteCallback(
        action='end', amount=amount))

    # Настраиваем сетку кнопок (например, 1 сверху, 2 посередине, 1 снизу...)
    # Здесь сделаем по 2 кнопки в ряд, а последнюю (End) отдельно
    builder.adjust(1, 2, 1, 1, 1)

    return builder.as_markup()

# --- Хендлеры ---


@router.message(Command("control"), F.from_user.id == ADMIN_ID)
async def cmd_control(message: types.Message):
    await message.answer(
        'Панель управления:',
        reply_markup=get_keyboard(amount=0)
    )

# Обработка нажатий кнопок
# Мы фильтруем по нашему классу VoteCallback и сразу распаковываем callback_data


@router.callback_query(VoteCallback.filter(F.action == 'up'))
async def vote_up_cb(call: types.CallbackQuery):
    # Используем to_thread, чтобы pyautogui не блокировал бота
    await asyncio.to_thread(pag.press, 'up')
    # Обязательно отвечать на колбэк, чтобы убрались "часики" на кнопке
    await call.answer()


@router.callback_query(VoteCallback.filter(F.action == 'down'))
async def vote_down_cb(call: types.CallbackQuery):
    await asyncio.to_thread(pag.press, 'down')
    await call.answer()


@router.callback_query(VoteCallback.filter(F.action == 'left'))
async def vote_left_cb(call: types.CallbackQuery):
    await asyncio.to_thread(pag.press, 'left')
    await call.answer()


@router.callback_query(VoteCallback.filter(F.action == 'right'))
async def vote_right_cb(call: types.CallbackQuery):
    await asyncio.to_thread(pag.press, 'right')
    await call.answer()


@router.callback_query(VoteCallback.filter(F.action == 'pause'))
async def vote_pause_cb(call: types.CallbackQuery):
    await asyncio.to_thread(pag.press, 'playpause')
    await call.answer("Пауза/Пуск")


@router.callback_query(VoteCallback.filter(F.action == 'end'))
async def vote_end_cb(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Управление завершено.")
    # Удаляем сообщение с кнопками, чтобы не спамить
    await call.message.delete()
    # Очищаем состояние (аналог storage.finish())
    await state.clear()
    await call.answer()
