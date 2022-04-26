from aiogram import types, Dispatcher
from Handlers.State import Workkomp as ps
from aiogram.dispatcher import FSMContext
from Handlers.Handlers import bot, dp, id
from Keyboardz.KeybordsKomp import KeybordKomp
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup


class workcomand(StatesGroup):
    commamnd = State()


async def menuwork(message: types.Message):
    await workcomand.commamnd.set()
    await bot.send_message(id, "Работа с компьютером. Выберите действие", reply_markup=KeybordKomp)


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


def register_Handler_StateWork(dp: Dispatcher):
    dp.register_message_handler(menuwork, commands=['rabota'])
