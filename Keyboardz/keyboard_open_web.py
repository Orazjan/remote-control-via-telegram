from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb1 = KeyboardButton("Vk")
kb2 = KeyboardButton("YouTube")
kb3 = KeyboardButton("Закрыть окно")
kb4 = KeyboardButton("Открыть последнее окно")
kbdiff = KeyboardButton("Другой сайт")

keyboard_open = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_open.add(kb1, kb2, kb3).add(kb4, kbdiff)

