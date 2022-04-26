from Handlers import Opens
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from Handlers.Handlers import bot, dp, id
from Keyboardz.KeyboardOpenWeb import KeyboardOpen
from Handlers.State import OpenWeb as ow, ReturnMessage
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup

storage = MemoryStorage()

class opencomand(StatesGroup):
    commamnd = State()
    urlname = State()


async def menuWeb(message: types.Message):
    await opencomand.commamnd.set()
    await bot.send_message(id, "Открытие сайта. Выбрите сайт:\n", reply_markup=KeyboardOpen)


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

    Opens.openweb(data['urlname'])    
    await bot.send_message(id, ReturnMessage(f"Ссылка открыта \n"))
    await state.finish()
    if (ReplyKeyboardMarkup == True):
        ReplyKeyboardRemove.remove_keyboard

def register_Handler_StateOpen(dp: Dispatcher):
    dp.register_message_handler(menuWeb, commands=['openweb'])
    