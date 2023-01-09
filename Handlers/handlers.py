import platform
from aiogram import types, Dispatcher, Bot
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from environs import Env
import Handlers.state as st
import Handlers.funcs as fun

env = Env()
env.read_env()

identify = env.int('id')

bot = Bot(token=env.str('Api_Token'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def get_proc():
    if (platform.processor() == env.str("kompfirst")):
        proccessor = "Первый компьютер\n"
        return proccessor
    proccessor = f'Другой комп: {platform.processor()}\n'
    return proccessor


async def on_startup():
    await bot.send_message(identify, st.return_message(f"Компьютер \n{get_proc()} \nвключён в "), reply_markup=ReplyKeyboardRemove())


async def working(message: types.message):
    await bot.send_message(identify, st.return_message(f"Работает: {get_proc()}\n"), reply_markup=ReplyKeyboardRemove())


async def cancel(message: types.Message):
    await bot.send_message(identify, st.return_message("Отмена действия "))
    fun.cancel()


async def help(message: types.Message):
    await bot.send_message(identify, fun.help())


async def kill(message: types.Message):
    await bot.send_message(identify, st.return_message("Программа отключается "))
    fun.kill_func()


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(working, commands=['start'])
    dp.register_message_handler(cancel, commands=['cancel'])
    dp.register_message_handler(kill, commands=['kill'])
    dp.register_message_handler(help, commands=['help'])
