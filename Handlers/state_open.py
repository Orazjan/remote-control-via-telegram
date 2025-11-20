from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from environs import Env

from Funcs import BrowserCommands
from Funcs.state import return_message
from Keyboardz.keyboard_open_web import keyboard_open
from message_processing.open_messages import open_web as ow

env = Env()
env.read_env()
ADMIN_ID = env.int('id')

router = Router()


class OpenWebStates(StatesGroup):
    waiting_for_selection = State()
    waiting_for_url = State()


@router.message(Command("openweb"), F.from_user.id == ADMIN_ID)
async def cmd_open_web(message: types.Message, state: FSMContext):
    await state.set_state(OpenWebStates.waiting_for_selection)
    await message.answer("Выберите сайт:", reply_markup=keyboard_open)


@router.message(OpenWebStates.waiting_for_selection, F.from_user.id == ADMIN_ID)
async def process_selection(message: types.Message, state: FSMContext):
    selected_site = message.text

    if selected_site == "Другой сайт":
        await state.set_state(OpenWebStates.waiting_for_url)
        response_text = await ow(selected_site)
        await message.answer(response_text, reply_markup=types.ReplyKeyboardRemove())

    else:
        response_text = await ow(selected_site)
        await message.answer(response_text, reply_markup=types.ReplyKeyboardRemove())
        await state.clear()


@router.message(OpenWebStates.waiting_for_url, F.from_user.id == ADMIN_ID)
async def process_url_input(message: types.Message, state: FSMContext):
    url_input = message.text
    try:
        await BrowserCommands.BrowserCommands.open_web(url_input)
        await message.answer(return_message("Ссылка открыта \n"), reply_markup=types.ReplyKeyboardRemove())
    except Exception as e:
        await message.answer(f"Ошибка: {e}")

    await state.clear()
