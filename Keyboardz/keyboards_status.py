from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb1 = KeyboardButton("Батарея")
kb4 = KeyboardButton("Закрыть окно")
kb2 = KeyboardButton("Открытые программы")
kb3 = KeyboardButton("Закрыть программу")
kb5 = KeyboardButton("Логи")

keybord_status = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True)
keybord_status.add(kb1, kb4).add(kb2, kb3, kb5)
