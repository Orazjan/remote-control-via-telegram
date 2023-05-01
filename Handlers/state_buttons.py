from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from Handlers.handlers import bot, dp, identify
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from Keyboardz.keyboards_commands import keyboard_commands
from Funcs import button_command

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

    if message.text == "ALT F4":
        await bot.send_message(identify, "ALT F4")
        command_funcs.commands.closealt()
        await state.finish()

    elif message.text == "ALT TAB":
        await bot.send_message(identify, "ALT TAB")
        command_funcs.commands.alttab()
        await state.finish()
        
    elif message.text == "F5":
        await bot.send_message(identify, "F5")
        command_funcs.commands.F5()
        await state.finish()
        
    else:
        await bot.send_message(identify, "Неправильная команда")
        await state.finish()

    ReplyKeyboardRemove.remove_keyboard = True


def register_handler_state_button(dp: Dispatcher):
    dp.register_message_handler(button_command, commands=['comands'])
