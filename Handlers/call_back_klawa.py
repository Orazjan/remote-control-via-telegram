import asyncio
import logging
import pyautogui as pag
from Handlers.handlers import bot, dp, Dispatcher, identify
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import MessageNotModified

loop = asyncio.get_event_loop()
storage = MemoryStorage()
dp.middleware.setup(LoggingMiddleware())

vote_cb = CallbackData('vote', 'action', 'amount')  # post:<action>:<amount>

def get_keyboard(amount):
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton('up', callback_data=vote_cb.new(action='up', amount=amount))).add(
        types.InlineKeyboardButton('left', callback_data=vote_cb.new(action='left', amount=amount)),
        types.InlineKeyboardButton('right', callback_data=vote_cb.new(action='right', amount=amount))).add(
        types.InlineKeyboardButton('down', callback_data=vote_cb.new(action='down', amount=amount))).add(
        types.InlineKeyboardButton('end', callback_data=vote_cb.new(action='end', amount=amount)))


async def cmd_control(message: types.Message):
    await bot.send_message(identify, 'Выбирайте действие: ', reply_markup=get_keyboard(0))


@dp.callback_query_handler(vote_cb.filter(action='up'))
async def vote_up_cb_handler(query: types.CallbackQuery, callback_data: dict):
    logging.info(callback_data)
    amount = int(callback_data['amount'])
    pag.press('up')
    await bot.send_message(f'You voted up! Now you have {amount} votes.',
                                query.from_user.id,
                                query.message.message_id,
                                reply_markup=get_keyboard(amount))


@dp.callback_query_handler(vote_cb.filter(action='down'))
async def vote_down_cb_handler(query: types.CallbackQuery, callback_data: dict):
    pag.press('down')
    amount = int(callback_data['amount'])
    await bot.send_message(f'You voted up! Now you have {amount} votes.',
                                query.from_user.id,
                                query.message.message_id,
                                reply_markup=get_keyboard(amount))


@dp.callback_query_handler(vote_cb.filter(action='left'))
async def vote_down_cb_handler(query: types.CallbackQuery, callback_data: dict):
    amount = int(callback_data['amount'])
    pag.press('left')
    await bot.send_message(f'You voted down! Now you have {amount} votes.',
                                query.from_user.id,
                                query.message.message_id,
                                reply_markup=get_keyboard(amount))

@dp.callback_query_handler(vote_cb.filter(action='right'))
async def vote_down_cb_handler(call: types.CallbackQuery):
    pag.press('right')
    
@dp.callback_query_handler(vote_cb.filter(action='end'))
async def vote_down_cb_handler(call: types.CallbackQuery):
    await call.answer("Thanks")

@dp.errors_handler(exception=MessageNotModified)  # for skipping this exception
async def message_not_modified_handler(update, error):
    return True

def register_handler_control(dp: Dispatcher):
    dp.register_message_handler(cmd_control, commands=['control'])
    