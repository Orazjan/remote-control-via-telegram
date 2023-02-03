from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# kb1 = KeyboardButton("Напечатать")
kb2 = KeyboardButton("Рандом с мышкой")
kb3 = KeyboardButton("Вывод окна")
kb4 = KeyboardButton("Скриншот экрана")
# kb5 = KeyboardButton("Нажать на кнопку")
kbdiff = KeyboardButton("Другое")

keyBoard_funs = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyBoard_funs.add(kb2, kb3).add(kb4, kbdiff)

keyb1 = KeyboardButton("Программа перестала отвечать!\nПерезагрузите компьютер!")
keyb2 = KeyboardButton("Мало места. Удалите ненужные программы")
keyboard_wybor = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_wybor.add(keyb1).add(keyb2)
