from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb1 = KeyboardButton("Батарея")
kb6 = KeyboardButton("Яркость")
kb7 = KeyboardButton("Звук")
# kb4 = KeyboardButton("")
kb2 = KeyboardButton("Открытые программы")
kb3 = KeyboardButton("Закрыть программу")
kb5 = KeyboardButton("Логи")

keybord_status = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True)
keybord_status.add(kb1, kb6).add(kb7, kb2, kb3).add(kb5)
