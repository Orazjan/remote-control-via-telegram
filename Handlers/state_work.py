from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
from message_processing import work_messages as ps

from Handlers.handlers import bot, dp, identify
from Keyboardz import keybords_komp
import pyautogui as pag
import random as rd

class work_comands(StatesGroup):
    commamnd = State()
    set_secconds = State()

async def menu_work(message: types.Message):
    if (message.from_id != identify):
        await bot.send_message(message.from_user.id, "Неправильная команда")
    else:
        await work_comands.commamnd.set()
        await bot.send_message(identify, "Работа с компьютером. Выберите действие", reply_markup=keybords_komp.keybord_komp)

@dp.message_handler(state=work_comands.commamnd)
async def process_name(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['comandname'] = message.text

    if data['comandname'] == 'Покинуть систему':
        hren = data['comandname']
        await bot.send_message(identify, ps.work_message.work_komp(hren))
        await state.finish()
    elif data['comandname'] == 'Заблокировать экран':
        hren = data['comandname']
        await bot.send_message(identify, ps.work_message.work_komp(hren))
        await state.finish()
        
    else:
        hren = data['comandname']
        await work_comands.next()
        await bot.send_message(identify, ps.work_message.work_komp(hren))
        await work_comands.set_secconds.set()

    ReplyKeyboardRemove.remove_keyboard = True

@dp.message_handler(state=work_comands.set_secconds)
async def set_seconds(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['set_seccond'] = message.text
    await bot.send_message(identify, ps.work_message.perezagruzka(data['comandname'], data['set_seccond']))
    await state.finish()
    ReplyKeyboardRemove.remove_keyboard = True

def register_handler_state_work(dp: Dispatcher):
    dp.register_message_handler(menu_work, commands=['rabota'])
