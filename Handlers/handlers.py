import platform
from aiogram import Router, types, F
from aiogram.filters import Command, CommandStart
from environs import Env
import Funcs.state as st
import Funcs.funcs as fun

env = Env()
env.read_env()
ADMIN_ID = env.int('id')
COMP_NAME = env.str("kompfirst", "MyPC")

router = Router()


def get_proc():
    proc_name = platform.processor()
    if proc_name == COMP_NAME:
        return "Первый компьютер\n"
    return f'Другой комп: {proc_name}\n'


@router.message(CommandStart(), F.from_user.id == ADMIN_ID)
async def working(message: types.Message):
    info = f"Работает: {get_proc()}\n{st.start_time}"
    await message.answer(info, reply_markup=types.ReplyKeyboardRemove())


@router.message(Command("cancel"), F.from_user.id == ADMIN_ID)
async def cancel(message: types.Message):
    await message.answer(st.return_message("Отмена действия "))
    fun.cancel_shutdown()


@router.message(Command("kill"), F.from_user.id == ADMIN_ID)
async def kill(message: types.Message):
    await message.answer(st.return_message("Программа отключается "))
    fun.kill_bot_process()


@router.message(Command("help"), F.from_user.id == ADMIN_ID)
async def help_command(message: types.Message):
    await message.answer(fun.get_help_text())
