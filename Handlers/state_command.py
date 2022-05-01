from aiogram import types, Dispatcher
from Handlers.funcs import kill_process
from aiogram.dispatcher import FSMContext
from Handlers.handlers import bot, dp, id
from Keyboardz.keyboards_status import keybord_status
from Handlers.state import status_komp as ps, return_message
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup

storage = MemoryStorage()

class statecomand(StatesGroup):
    commandforstatus = State()
    taskname = State()

async def menustatus(message: types.Message):
    await statecomand.commandforstatus.set()
    await bot.send_message(id, "Работа со статусом компьютера. Выберите действие", reply_markup=keybord_status)


@dp.message_handler(state=statecomand.commandforstatus)
async def process_command(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['commandforstatus'] = message.text

    if (ReplyKeyboardMarkup == True):
        ReplyKeyboardRemove.remove_keyboard

    if (data['commandforstatus'] != "Закрыть программу"):
        hren = data['commandforstatus']
        await bot.send_message(id, ps(hren))
        await state.finish()
    else:        
        await statecomand.next()
        await bot.send_message(id, return_message("Введите название программы\n"))
        await statecomand.taskname.set()

@dp.message_handler(state=statecomand.taskname)
async def procces_task(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['taskname'] = message.text

    kill_process(data['taskname'])    
    await bot.send_message(id, return_message(f"Удалено {data['taskname']}\n"))
    await state.finish()
    if (ReplyKeyboardMarkup == True):
        ReplyKeyboardRemove.remove_keyboard

def register_handler_state_command(dp: Dispatcher):
    dp.register_message_handler(menustatus, commands=['status'])
