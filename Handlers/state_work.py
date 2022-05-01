from aiogram import types, Dispatcher
from Handlers.state import work_komp as ps
from aiogram.dispatcher import FSMContext
from Handlers.handlers import bot, dp, id
from Keyboardz.keybords_komp import keybord_komp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup


class workcomand(StatesGroup):
    commamnd = State()


async def menu_work(message: types.Message):
    await workcomand.commamnd.set()
    await bot.send_message(id, "Работа с компьютером. Выберите действие", reply_markup=keybord_komp)


@dp.message_handler(state=workcomand.commamnd)
async def process_name(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['comandname'] = message.text

    await workcomand.next()
    if (ReplyKeyboardMarkup == True):
        ReplyKeyboardRemove.remove_keyboard

    hren = data['comandname']
    await bot.send_message(id, ps(hren))
    await state.finish()


def register_handler_state_work(dp: Dispatcher):
    dp.register_message_handler(menu_work, commands=['rabota'])
