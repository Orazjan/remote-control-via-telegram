from Handlers import Funcs
from Keyboardz.KeyboardFun import *
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from Handlers.Handlers import bot, dp, id
from Handlers.State import FunSegment as fs, ReturnMessage
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup

storage = MemoryStorage()

class statecomand(StatesGroup):
    commandforfun = State()
    zadacha = State()

async def menufun(message: types.Message):
    await statecomand.commandforfun.set()
    await bot.send_message(id, "Глава интересное. Выберите действие", reply_markup=KeyBoardFuns)

@dp.message_handler(state=statecomand.commandforfun)
async def fun_command(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['choosen'] = message.text

    if data['choosen']=="Скриншот экрана":
        Funcs.Screenshot()
        photo = open('D://Projects/PY/ForBot/screens/ss.png', 'rb')
        await bot.send_photo(id, photo) 

    if (data['choosen'].startswith("Вывод")):
        await bot.send_message(id, fs(message.text), reply_markup=keyboardwybor)
    else:
        await bot.send_message(id, fs(data['choosen']))
    
    await statecomand.next()
    await statecomand.zadacha.set()

    if (ReplyKeyboardMarkup == True):
        ReplyKeyboardRemove.remove_keyboard   

@dp.message_handler(state=statecomand.zadacha)
async def second(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['values'] = message.text

    if(data['choosen'] == "Рандом с мышкой"):
        hren = data['values']
        Funcs.MouseRand(hren)
        await bot.send_message(id, ReturnMessage(f"Процесс готово.\n"))

    elif (data['choosen'] == "Напечатать"):
        hren = data['values']
        Funcs.WriteText(hren)
        await bot.send_message(id, ReturnMessage(f"Процесс {data['values']} готово.\n"))
    
    elif (data['choosen'] == "Вывод окна"):
        hren = data['values']
        Funcs.WindowWarning(hren)
        await bot.send_message(id, ReturnMessage(f"Процесс готово.\n"))
    
    elif (data['choosen'] == "Скриншот экрана"): 
        await bot.send_message(id, ReturnMessage(f"Выбирайте действие.\n"))

    await state.finish()

    if (ReplyKeyboardMarkup == True):
        ReplyKeyboardRemove.remove_keyboard


def register_Handler_FunCommand(dp: Dispatcher):
    dp.register_message_handler(menufun, commands=['funfun'])
    