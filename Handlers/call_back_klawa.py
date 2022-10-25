import asyncio
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import MessageNotModified
import pyautogui as pag
from Handlers.handlers import bot, dp, Dispatcher, identify

loop = asyncio.get_event_loop()
storage = MemoryStorage()
dp.middleware.setup(LoggingMiddleware())

vote_cb = CallbackData('vote', 'action', 'amount')  # post:<action>:<amount>


def get_keyboard(amount):
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton('up', callback_data=vote_cb.new(action='up', amount=amount))).add(
        types.InlineKeyboardButton(
            'left', callback_data=vote_cb.new(action='left', amount=amount)),
        types.InlineKeyboardButton('right', callback_data=vote_cb.new(action='right', amount=amount))).add(
        types.InlineKeyboardButton('down', callback_data=vote_cb.new(action='down', amount=amount))).add(
        types.InlineKeyboardButton('play\pause', callback_data=vote_cb.new(action='pause', amount=amount))).add(
        types.InlineKeyboardButton('end', callback_data=vote_cb.new(action='end', amount=amount)))


async def cmd_control(message: types.Message):
    await bot.send_message(identify, 'Выбирайте действие: ', reply_markup=get_keyboard(0))


@dp.callback_query_handler(vote_cb.filter(action='up'))
async def vote_up_cb_handler(call: types.CallbackQuery):
    pag.press('up')


@dp.callback_query_handler(vote_cb.filter(action='down'))
async def vote_down_cb_handler(call: types.CallbackQuery):
    pag.press('down')


@dp.callback_query_handler(vote_cb.filter(action='left'))
async def vote_down_cb_handler(call: types.CallbackQuery):
    pag.press('left')


@dp.callback_query_handler(vote_cb.filter(action='right'))
async def vote_down_cb_handler(call: types.CallbackQuery):
    pag.press('right')


@dp.callback_query_handler(vote_cb.filter(action='pause'))
async def vote_down_cb_handler(call: types.CallbackQuery):
    pag.press('playpause')


@dp.callback_query_handler(vote_cb.filter(action='end'))
async def vote_down_cb_handler(call: types.CallbackQuery):
    await bot.send_message(identify, "Выберите команду: ")
    await storage.finish()


@dp.errors_handler(exception=MessageNotModified)  # for skipping this exception
async def message_not_modified_handler(update, error):
    await storage.finish()
    return True


def register_handler_control(dp: Dispatcher):
    dp.register_message_handler(cmd_control, commands=['control'])
