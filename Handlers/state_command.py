from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from Handlers.handlers import bot, dp, identify
from Keyboardz.keyboards_status import keybord_status
from Funcs.state import return_message
from message_processing import status_messages as sc
from Funcs import status_commands as sac

storage = MemoryStorage()


class StateComand(StatesGroup):
    commandforstatus = State()
    taskname = State()


async def menustatus(message: types.Message):
    if (message.from_id != identify):
        await bot.send_message(message.from_user.id, "Неправильная команда")
    else:
        await StateComand.commandforstatus.set()
        await bot.send_message(identify, "Работа со статусом компьютера. Выберите действие", reply_markup=keybord_status)


@dp.message_handler(state=StateComand.commandforstatus)
async def process_command(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['commandforstatus'] = message.text

    ReplyKeyboardRemove.remove_keyboard = True

    if data['commandforstatus'] == "Закрыть программу":
        await StateComand.next()
        await bot.send_message(identify, sc.status_message.status_komp(data['commandforstatus']))
        await StateComand.taskname.set()

    elif data['commandforstatus'] == "Яркость":
        await StateComand.next()
        await bot.send_message(identify, sc.status_message.status_komp(data['commandforstatus']))
        await StateComand.taskname.set()

    elif data['commandforstatus'] == "Звук":
        await StateComand.next()
        await bot.send_message(identify, sc.status_message.status_komp(data['commandforstatus']))
        await StateComand.taskname.set()

    elif data['commandforstatus'] == "Логи":
        hren = data['commandforstatus']
        doc = open(f'{funcs.PATH}logfile.log', 'rb')
        await bot.send_document(identify, doc)
        await bot.send_message(identify, sc.status_message.status_komp(hren))
        await state.finish()

    else:
        hren = data['commandforstatus']
        await bot.send_message(identify, sc.status_message.status_komp(hren))
        await state.finish()


@dp.message_handler(state=StateComand.taskname)
async def procces_task(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['taskname'] = message.text

    if data['commandforstatus'] == "Закрыть программу":
        sac.status_Commands.kill_process(data['taskname'])
        await bot.send_message(identify, return_message(f"Удалено {data['taskname']}\n"))
        await state.finish()

    elif data['commandforstatus'] == "Яркость":
        sac.status_Commands.bright_monitor(data['taskname'])
        await bot.send_message(identify, return_message(f"Яркость установлена на {data['taskname']}%\n"))
        await state.finish()

    elif data['commandforstatus'] == "Звук":
        sac.status_Commands.volume(data['taskname'])
        await bot.send_message(identify, return_message(f"Звук установлен на {data['taskname']}%\n"))
        await state.finish()

    ReplyKeyboardRemove.remove_keyboard = True


def register_handler_state_command(dp: Dispatcher):
    dp.register_message_handler(menustatus, commands=['status'])
