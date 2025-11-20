from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from environs import Env

from Keyboardz.keyboards_commands import keyboard_commands
from message_processing import button_messages as bm

env = Env()
env.read_env()
ADMIN_ID = env.int('id')

router = Router()


class ButtonsStates(StatesGroup):
    waiting_for_command = State()


@router.message(Command("comands"), F.from_user.id == ADMIN_ID)
async def cmd_start_buttons(message: types.Message, state: FSMContext):
    await state.set_state(ButtonsStates.waiting_for_command)
    await message.answer("Выберите команду:", reply_markup=keyboard_commands)


@router.message(ButtonsStates.waiting_for_command, F.from_user.id == ADMIN_ID)
async def process_command_state(message: types.Message, state: FSMContext):
    command_text = message.text

    response_text = await bm.ButtonMessages.button_segment(command_text)

    await message.answer(response_text, reply_markup=types.ReplyKeyboardRemove())
    await state.clear()
