from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
from Handlers.state import work_komp as ps, perezagruzka
from Handlers.handlers import bot, dp, identify
from Keyboardz import keybords_komp, keyboard_call_back
import pyautogui as pag
import random as rd

class work_comands(StatesGroup):
    commamnd = State()
    set_secconds = State()

async def menu_work(message: types.Message):
    await work_comands.commamnd.set()
    await bot.send_message(identify, "Работа с компьютером. Выберите действие", reply_markup=keybords_komp.keybord_komp)

@dp.message_handler(state=work_comands.commamnd)
async def process_name(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['comandname'] = message.text

    if data['comandname'] == 'Покинуть систему':
        hren = data['comandname']
        await bot.send_message(identify, ps(hren))
        await state.finish()
    else:
        hren = data['comandname']
        await work_comands.next()
        await bot.send_message(identify, ps(hren))
        await work_comands.set_secconds.set()

    ReplyKeyboardRemove.remove_keyboard = True

@dp.message_handler(state=work_comands.set_secconds)
async def set_seconds(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['set_seccond'] = message.text
    await bot.send_message(identify, perezagruzka(data['comandname'], data['set_seccond']))
    await state.finish()
    ReplyKeyboardRemove.remove_keyboard = True

"""call back"""

@dp.message_handler(commands="random")
async def cmd_random(message: types.Message):
    # keyboard = types.InlineKeyboardMarkup()
    # keyboard.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
    await message.answer("Нажмите на кнопку, чтобы управлять клавиатурой", reply_markup=keyboard_call_back.get_keyboard(), callback_data='up')

@dp.callback_query_handler(text = 'up')
async def send_random_value(call: types.CallbackQuery):
    await call.message.answer(str(rd.randint(1, 10)))
    await call.answer(text="Спасибо, что воспользовались ботом!", show_alert=True)
    # или просто await call.answer()



"""end call back
"""
def register_handler_state_work(dp: Dispatcher):
    dp.register_message_handler(menu_work, commands=['rabota'])
