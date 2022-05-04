from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup
from Handlers.state import work_komp as ps, perezagruzka
from Handlers.handlers import bot, dp, id
from Keyboardz.keybords_komp import keybord_komp

class work_comands(StatesGroup):
    commamnd = State()
    set_secconds = State()

async def menu_work(message: types.Message):
    await work_comands.commamnd.set()
    await bot.send_message(id, "Работа с компьютером. Выберите действие", reply_markup=keybord_komp)

@dp.message_handler(state=work_comands.commamnd)
async def process_name(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['comandname'] = message.text

    if data['comandname'] == 'Покинуть систему':
        hren = data['comandname']
        await bot.send_message(id, ps(hren))
        await state.finish()
    else:
        hren = data['comandname']
        await work_comands.next()
        await bot.send_message(id, ps(hren))
        await work_comands.set_secconds.set()

    ReplyKeyboardRemove.remove_keyboard = True

@dp.message_handler(state=work_comands.set_secconds)
async def set_seconds(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['set_seccond'] = message.text
    await bot.send_message(id, perezagruzka(data['comandname'], data['set_seccond']))
    await state.finish()
    ReplyKeyboardRemove.remove_keyboard = True

def register_handler_state_work(dp: Dispatcher):
    dp.register_message_handler(menu_work, commands=['rabota'])
