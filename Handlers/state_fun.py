from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from Handlers.handlers import bot, dp, id
from Handlers import funcs
from Keyboardz.keyboard_fun import *
from Handlers.state import fun_segment as fs, return_message

storage = MemoryStorage()

class statecomand(StatesGroup):
    commandforfun = State()
    zadacha = State()

async def menu_fun(message: types.Message):
    await statecomand.commandforfun.set()
    await bot.send_message(id, "Глава интересное. Выберите действие", reply_markup=keyBoard_funs)

@dp.message_handler(state=statecomand.commandforfun)
async def fun_command(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['choosen'] = message.text

    if data['choosen']=="Скриншот экрана":
        funcs.screenshot()
        photo = open(f'{funcs.PATH}/ss.png', 'rb')
        await bot.send_photo(id, photo)
        await bot.send_message(id, return_message("Скриншот готов\n"))
        await state.finish()

    elif data['choosen']== "Вывод окна":
        await bot.send_message(id, fs(message.text), reply_markup=keyboard_wybor)
        await statecomand.next()
        await statecomand.zadacha.set()
    else:
        await bot.send_message(id, fs(data['choosen']))
        await statecomand.next()
        await statecomand.zadacha.set()

    ReplyKeyboardRemove.remove_keyboard = True

@dp.message_handler(state=statecomand.zadacha)
async def second(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['values'] = message.text

    if(data['choosen'] == "Рандом с мышкой"):
        hren = data['values']
        funcs.mouse_rand(hren)
        await bot.send_message(id, return_message(f"Процесс готово.\n"))

    elif (data['choosen'] == "Напечатать"):
        hren = data['values']
        funcs.write_text(hren)
        await bot.send_message(id, return_message(f"Процесс {data['values']} готово.\n"))

    elif (data['choosen'] == "Вывод окна"):
        hren = data['values']
        funcs.window_warning(hren)
        await bot.send_message(id, return_message(f"Процесс готово.\n"))

    await state.finish()

    if (ReplyKeyboardMarkup == True):
        ReplyKeyboardRemove.remove_keyboard


def register_handler_fun_command(dp: Dispatcher):
    dp.register_message_handler(menu_fun, commands=['funfun'])
    