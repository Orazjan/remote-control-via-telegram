from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb1 = KeyboardButton("Батарея")
kb2 = KeyboardButton("Открытые программы")
kb3 = KeyboardButton("Закрыть программу")

KeybordStatus = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True)
KeybordStatus.add(kb1).add(kb2, kb3)
