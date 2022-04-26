from aiogram import types, Dispatcher
from Handlers.Funcs import KillProcess
from aiogram.dispatcher import FSMContext
from Handlers.Handlers import bot, dp, id
from Keyboardz.KeyboardsStatus import KeybordStatus
from Handlers.State import StatusKomp as ps, ReturnMessage
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup

storage = MemoryStorage()

class statecomand(StatesGroup):
    commandforstatus = State()
    taskname = State()

async def menustatus(message: types.Message):
    await statecomand.commandforstatus.set()
    await bot.send_message(id, "Работа со статусом компьютера. Выберите действие", reply_markup=KeybordStatus)


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
        await bot.send_message(id, ReturnMessage("Введите название программы\n"))
        await statecomand.taskname.set()

@dp.message_handler(state=statecomand.taskname)
async def procces_task(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        data['taskname'] = message.text

    KillProcess(data['taskname'])    
    await bot.send_message(id, ReturnMessage(f"Удалено {data['taskname']}\n"))
    await state.finish()
    if (ReplyKeyboardMarkup == True):
        ReplyKeyboardRemove.remove_keyboard

def register_Handler_Statecommand(dp: Dispatcher):
    dp.register_message_handler(menustatus, commands=['status'])
