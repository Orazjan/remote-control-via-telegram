from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from environs import Env

from message_processing import work_messages as ps
from Keyboardz import keybords_komp

env = Env()
env.read_env()
ADMIN_ID = env.int('id')

router = Router()


class WorkStates(StatesGroup):
    waiting_for_action = State()
    waiting_for_timer = State()


@router.message(Command("rabota"), F.from_user.id == ADMIN_ID)
async def cmd_work_start(message: types.Message, state: FSMContext):
    await state.set_state(WorkStates.waiting_for_action)
    await message.answer("Меню питания:", reply_markup=keybords_komp.keybord_komp)


@router.message(WorkStates.waiting_for_action, F.from_user.id == ADMIN_ID)
async def process_work_action(message: types.Message, state: FSMContext):
    action_name = message.text
    await state.update_data(command_name=action_name)

    instant_actions = ['Покинуть систему', 'Заблокировать экран']

    if action_name in instant_actions:
        # ВАЖНО: await
        response_text = await ps.WorkMessages.work_komp(action_name)
        await message.answer(response_text, reply_markup=types.ReplyKeyboardRemove())
        await state.clear()
    else:
        await state.set_state(WorkStates.waiting_for_timer)
        # ВАЖНО: await
        response_text = await ps.WorkMessages.work_komp(action_name)
        await message.answer(f"{response_text}", reply_markup=types.ReplyKeyboardRemove())


@router.message(WorkStates.waiting_for_timer, F.from_user.id == ADMIN_ID)
async def process_timer_input(message: types.Message, state: FSMContext):
    timer_seconds = message.text
    data = await state.get_data()
    action_name = data.get('command_name')

    # ВАЖНО: await
    response_text = await ps.WorkMessages.perezagruzka(action_name, timer_seconds)

    await message.answer(response_text, reply_markup=types.ReplyKeyboardRemove())
    await state.clear()
