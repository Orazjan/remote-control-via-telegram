import platform
from environs import Env
import Handlers.State as fun
from aiogram import types, Dispatcher, Bot
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage

env = Env()
env.read_env()

id=env.int('id')

bot = Bot(token=env.str('Api_Token'))
storage = MemoryStorage()
dp = Dispatcher(bot,storage=storage)
proccessor = ''

def getproc():
    if (platform.processor()==env.str("kompfirst")):
        global proccessor
        proccessor = "Первый компьютер"
        return proccessor


async def on_startup():
    await bot.send_message(id, fun.ReturnMessage(f"Компьютер \n{getproc()} \nвключён в "),reply_markup=ReplyKeyboardRemove())


async def working(message: types.message):
    await bot.send_message(id, fun.ReturnMessage(f"Работает: {proccessor}\n"),reply_markup=ReplyKeyboardRemove())


async def cancel(message: types.Message):
    await bot.send_message(id, fun.ReturnMessage("Отмена действия "))
    fun.Cancel()


async def kill(message: types.Message):
    await bot.send_message(id, fun.ReturnMessage("Программа отключается "))
    fun.KillFunc()

def register_Handler_Client(dp: Dispatcher):
    dp.register_message_handler(working, commands=['start'])
    dp.register_message_handler(cancel, commands=['cancel'])
    dp.register_message_handler(kill, commands=['kill'])
