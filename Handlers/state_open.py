from Handlers import opens
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from Handlers.handlers import bot, dp, id
from Keyboardz.keyboard_open_web import keyboard_open
from Handlers.state import open_web as ow, return_message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup

storage = MemoryStorage()

class opencomand(StatesGroup):
    commamnd = State()
    urlname = State()


async def menu_web(message: types.Message):
    await opencomand.commamnd.set()
    await bot.send_message(id, "Открытие сайта. Выбрите сайт:\n", reply_markup=keyboard_open)


@dp.message_handler(state=opencomand.commamnd)
async def process_command(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['comandn'] = message.text
    
    if (message.text != "Другой сайт"):
        
        hren = data['comandn']
        await bot.send_message(id, ow(hren))
        await state.finish()
    
    else:
        await opencomand.next()
        await bot.send_message(id, "Введите ссылку\n")
        await opencomand.urlname.set()

    
    if (ReplyKeyboardMarkup == True):
        ReplyKeyboardRemove.remove_keyboard


@dp.message_handler(state=opencomand.urlname)
async def procces_task(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['urlname'] = message.text

    opens.open_web(data['urlname'])    
    await bot.send_message(id, return_message(f"Ссылка открыта \n"))
    await state.finish()
    if (ReplyKeyboardMarkup == True):
        ReplyKeyboardRemove.remove_keyboard

def register_handler_state_open(dp: Dispatcher):
    dp.register_message_handler(menu_web, commands=['openweb'])
    