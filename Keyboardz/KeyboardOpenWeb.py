from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb1 = KeyboardButton("Vk")
kb2 = KeyboardButton("YouTube")
kbdiff = KeyboardButton("Другой сайт")

KeyboardOpen = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
KeyboardOpen.add(kb1, kb2).add(kbdiff)

