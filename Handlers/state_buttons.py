from aiogram import types, Dispatcher

from aiogram.types import ReplyKeyboardRemove

from Handlers.handlers import bot, dp, identify
from Keyboardz.keyboards_commands import keyboard_commands
from Handlers.state import return_message, status_komp as ps
from Handlers import funcs

async def comands(message: types.Message):
    await bot.send_message(identify, return_message("Выберите команду для исполнения "), reply_markup=keyboard_commands)
    

ReplyKeyboardRemove.remove_keyboard = True

def register_handler_state_button(dp: Dispatcher):
    dp.register_message_handler(comands, commands=['comands'])
