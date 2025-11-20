from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

builder_funs = ReplyKeyboardBuilder()

# Добавляем кнопки по очереди
builder_funs.button(text="Рандом с мышкой")
builder_funs.button(text="Вывод окна")
builder_funs.button(text="Скриншот экрана")
builder_funs.button(text="Фото с камеры")
builder_funs.button(text="Блок мышки и клавы")
builder_funs.button(text="Анблок мышки и клавы")
builder_funs.button(text="Другое")

# Настраиваем сетку
builder_funs.adjust(2, 2, 3)

keyBoard_funs = builder_funs.as_markup(
    resize_keyboard=True, one_time_keyboard=True)

builder_wybor = ReplyKeyboardBuilder()

builder_wybor.button(
    text="Программа перестала отвечать!\nПерезагрузите компьютер!")
builder_wybor.button(text="Мало места. Удалите ненужные программы")

builder_wybor.adjust(1)

keyboard_wybor = builder_wybor.as_markup(
    resize_keyboard=True, one_time_keyboard=True)
