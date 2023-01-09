from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb1 = KeyboardButton("ALT F4")
kb2 = KeyboardButton("ALT TAB")


keyboard_commands = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True)
keyboard_commands.add(kb1, kb2)
