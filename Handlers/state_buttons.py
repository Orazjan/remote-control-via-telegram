from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from Handlers.handlers import bot, dp, identify
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from Keyboardz.keyboards_commands import keyboard_commands
from Funcs import button_command
from message_processing import button_messages as bm

storage = MemoryStorage()


class buttons_commands(StatesGroup):
    commamnd = State()


async def button_command(message: types.Message):
    if (message.from_id != identify):
        await bot.send_message(message.from_user.id, "Неправильная команда")
    else:
        await buttons_commands.commamnd.set()
        await bot.send_message(identify, "Выберите команду\n", reply_markup=keyboard_commands)


@dp.message_handler(state=buttons_commands.commamnd)
async def process_command(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['comandn'] = message.text

    await bot.send_message(identify, bm.button_messages.button_segment(data['comandn']))
    await state.finish()

    await state.finish()
    ReplyKeyboardRemove.remove_keyboard = True


def register_handler_state_button(dp: Dispatcher):
    dp.register_message_handler(button_command, commands=['comands'])
