from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile
from environs import Env

import Funcs.funcs as funcs
from Funcs import status_commands as sac
from Funcs.state import return_message
from Keyboardz.keyboards_status import keybord_status
from message_processing import status_messages as sc

env = Env()
env.read_env()
ADMIN_ID = env.int('id')

router = Router()


class StatusStates(StatesGroup):
    waiting_for_command = State()
    waiting_for_argument = State()


@router.message(Command("status"), F.from_user.id == ADMIN_ID)
async def cmd_status_start(message: types.Message, state: FSMContext):
    await state.set_state(StatusStates.waiting_for_command)
    await message.answer("Меню статуса:", reply_markup=keybord_status)


@router.message(StatusStates.waiting_for_command, F.from_user.id == ADMIN_ID)
async def process_command_choice(message: types.Message, state: FSMContext):
    command_text = message.text
    await state.update_data(commandforstatus=command_text)

    commands_requiring_args = ["Закрыть программу", "Яркость", "Звук"]

    if command_text in commands_requiring_args:
        await state.set_state(StatusStates.waiting_for_argument)
        response_text = await sc.StatusMessage.status_komp(command_text)
        await message.answer(response_text, reply_markup=types.ReplyKeyboardRemove())

    elif command_text == "Логи":
        log_path = f'{funcs.PATH}logfile.log'
        try:
            log_file = FSInputFile(log_path)
            await message.answer_document(log_file)
            response_text = await sc.StatusMessage.status_komp(command_text)
            await message.answer(response_text, reply_markup=types.ReplyKeyboardRemove())
        except Exception as e:
            await message.answer(f"Нет логов или ошибка: {e}")
        await state.clear()

    else:
        response_text = await sc.StatusMessage.status_komp(command_text)
        await message.answer(response_text, reply_markup=types.ReplyKeyboardRemove())
        await state.clear()


@router.message(StatusStates.waiting_for_argument, F.from_user.id == ADMIN_ID)
async def process_task_argument(message: types.Message, state: FSMContext):
    task_argument = message.text
    data = await state.get_data()
    command_name = data.get('commandforstatus')

    if command_name == "Закрыть программу":
        await sac.StatusCommands.kill_process(task_argument)
        await message.answer(return_message(f"Удалено: {task_argument}"))

    elif command_name == "Яркость":
        await sac.StatusCommands.bright_monitor(task_argument)
        await message.answer(return_message(f"Яркость: {task_argument}%"))

    elif command_name == "Звук":
        await sac.StatusCommands.volume(task_argument)
        await message.answer(return_message(f"Звук: {task_argument}"))

    await state.clear()
