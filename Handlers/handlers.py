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
startTime = ""

def get_proc():
    if (platform.processor() == env.str("kompfirst")):
        proccessor = "Первый компьютер\n"
        return proccessor
    proccessor = f'Другой комп: {platform.processor()}\n'
    return proccessor


async def on_startup():
    await setup_bot_commands()
    startTime = st.return_time();
    await bot.send_message(identify, st.return_message(f"Компьютер \n{get_proc()} \nвключён в "), reply_markup=ReplyKeyboardRemove())

async def setup_bot_commands():
    bot_commands = [
        types.BotCommand(command="/start", description="Начать/перезапустить"),
        types.BotCommand(command="/help", description="Что я умею?"),
        types.BotCommand(command="/rabota", description="Работа компьютера"),
        types.BotCommand(command="/status",
                         description="Состояние компьютера"),
        types.BotCommand(command="/comands", description="Кнопки для быстрых действий"),
        types.BotCommand(command="/openweb", description="Открыть сайт"),
        types.BotCommand(command="/control", description="Для управления"),
        types.BotCommand(command="/kill", description="Отключить программу"),
        types.BotCommand(command="/cancel",
                         description="Отмена действия при выключении")
    ]
    await bot.set_my_commands(bot_commands)

async def working(message: types.message):
    if (message.from_id != identify):
        await bot.send_message(message.from_user.id, "Неправильная команда")
    else:
        await bot.send_message(identify, f"Работает: {get_proc()}\n {startTime}", reply_markup=ReplyKeyboardRemove())


async def cancel(message: types.Message):
    if (message.from_id != identify):
        await bot.send_message(message.from_user.id, "Неправильная команда")
    else:
        await bot.send_message(identify, st.return_message("Отмена действия "))
        fun.cancel()


async def help(message: types.Message):
    if (message.from_id != identify):
        await bot.send_message(message.from_user.id, "Неправильная команда")
    else:
        await bot.send_message(identify, fun.help())


async def kill(message: types.Message):
    if (message.from_id != identify):
        await bot.send_message(message.from_user.id, "Неправильная команда")
    else:
        await bot.send_message(identify, st.return_message("Программа отключается "))
        fun.kill_func()


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(working, commands=['start'])
    dp.register_message_handler(cancel, commands=['cancel'])
    dp.register_message_handler(kill, commands=['kill'])
    dp.register_message_handler(help, commands=['help'])
