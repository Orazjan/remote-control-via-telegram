from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from Handlers.handlers import bot, dp, id
from Keyboardz.keyboards_status import keybord_status
from Handlers.state import return_message, status_komp as ps
from Handlers import funcs

storage = MemoryStorage()

class StateComand(StatesGroup):
    commandforstatus = State()
    taskname = State()

async def menustatus(message: types.Message):
    await StateComand.commandforstatus.set()
    await bot.send_message(id, "Работа со статусом компьютера. Выберите действие", reply_markup=keybord_status)

@dp.message_handler(state=StateComand.commandforstatus)
async def process_command(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['commandforstatus'] = message.text

    ReplyKeyboardRemove.remove_keyboard = True

    if data['commandforstatus'] == "Закрыть программу":
        await StateComand.next()
        await bot.send_message(id, ps(data['commandforstatus']))
        await StateComand.taskname.set()

    elif data['commandforstatus'] == "Яркость":
        await StateComand.next()
        await bot.send_message(id, ps(data['commandforstatus']))
        await StateComand.taskname.set()

    elif data['commandforstatus'] == "Звук":
        await StateComand.next()
        await bot.send_message(id, ps(data['commandforstatus']))
        await StateComand.taskname.set()

    elif data['commandforstatus'] == "Логи":
        hren = data['commandforstatus']
        doc = open(f'{funcs.PATH}/logfile.log', 'rb')
        await bot.send_document(id, doc)
        await bot.send_message(id, ps(hren))
        await state.finish()

    else:
        hren = data['commandforstatus']
        await bot.send_message(id, ps(hren))
        await state.finish()

@dp.message_handler(state=StateComand.taskname)
async def procces_task(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['taskname'] = message.text

    if data['commandforstatus'] == "Закрыть программу":
        funcs.kill_process(data['taskname'])
        await bot.send_message(id, return_message(f"Удалено {data['taskname']}\n"))
        await state.finish()

    elif data['commandforstatus'] == "Яркость":
        funcs.bright_monitor(data['taskname'])
        await bot.send_message(id, return_message(f"Яркость установлена на {data['taskname']}%\n"))
        await state.finish()

    elif data['commandforstatus'] == "Звук":
        funcs.volume(data['taskname'])
        await bot.send_message(id, return_message(f"Звук установлен на {data['taskname']}%\n"))
        await state.finish()

    ReplyKeyboardRemove.remove_keyboard = True

def register_handler_state_command(dp: Dispatcher):
    dp.register_message_handler(menustatus, commands=['status'])
