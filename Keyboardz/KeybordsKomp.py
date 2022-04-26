from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb1 = KeyboardButton("Покинуть систему")
kb2 = KeyboardButton("Перезагрузка")
kb3 = KeyboardButton("Завершение работы")

KeybordKomp = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
KeybordKomp.add(kb1, kb2).add(kb3)
