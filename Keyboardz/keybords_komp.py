from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb1 = KeyboardButton("Покинуть систему")
kb2 = KeyboardButton("Перезагрузка")
kb3 = KeyboardButton("Завершение работы")

keybord_komp = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keybord_komp.add(kb1, kb2).add(kb3)
