import asyncio

import pyautogui as pag
from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from environs import Env

env = Env()
env.read_env()
ADMIN_ID = env.int('id')

router = Router()


class VoteCallback(CallbackData, prefix="vote"):
    action: str
    amount: int


def get_keyboard(amount: int):
    builder = InlineKeyboardBuilder()

    # Добавляем кнопки.
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
    builder.button(text='End', callback_data=VoteCallback(
        action='end', amount=amount))

    # Настраиваем сетку кнопок
    builder.adjust(1, 2, 1, 1, 1)

    return builder.as_markup()


@router.message(Command("control"), F.from_user.id == ADMIN_ID)
async def cmd_control(message: types.Message):
    await message.answer(
        'Панель управления:',
        reply_markup=get_keyboard(amount=0)
    )

# Обработка нажатий кнопок


@router.callback_query(VoteCallback.filter(F.action == 'up'))
async def vote_up_cb(call: types.CallbackQuery):
    await asyncio.to_thread(pag.press, 'up')
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
    await call.message.delete()
    # Очищаем состояние (аналог storage.finish())
    await state.clear()
    await call.answer()
