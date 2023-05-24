from Funcs import opens_commands
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from Handlers.handlers import bot, dp, identify
from Keyboardz.keyboard_open_web import keyboard_open
from message_processing.open_messages import open_web as ow
from Funcs.state import return_message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup

storage = MemoryStorage()


class opencomand(StatesGroup):
    commamnd = State()
    urlname = State()


async def menu_web(message: types.Message):
    if (message.from_id != identify):
        await bot.send_message(message.from_user.id, "Неправильная команда")
    else:
        await opencomand.commamnd.set()
        await bot.send_message(identify, "Открытие сайта. Выберите сайт:\n", reply_markup=keyboard_open)


@dp.message_handler(state=opencomand.commamnd)
async def process_command(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['comandn'] = message.text

    if message.text != "Другой сайт":
        await bot.send_message(identify, ow(data['comandn']))
        await state.finish()

    else:
        await opencomand.next()
        await bot.send_message(identify, ow(data['comandn']))
        await opencomand.urlname.set()

    ReplyKeyboardRemove.remove_keyboard = True


@dp.message_handler(state=opencomand.urlname)
async def procces_task(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['urlname'] = message.text

    opens.openingUrl.open_web((data['urlname']))
    await bot.send_message(identify, return_message(f"Ссылка открыта \n"))
    await state.finish()
    ReplyKeyboardRemove.remove_keyboard = True


def register_handler_state_open(dp: Dispatcher):
    dp.register_message_handler(menu_web, commands=['openweb'])
