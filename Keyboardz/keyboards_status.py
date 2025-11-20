from aiogram.utils.keyboard import ReplyKeyboardBuilder

builder = ReplyKeyboardBuilder()

# Добавляем кнопки по порядку
builder.button(text="Батарея")
builder.button(text="Яркость")
builder.button(text="Звук")
builder.button(text="Открытые программы")
builder.button(text="Закрыть программу")
builder.button(text="Логи")

# Настраиваем сетку
builder.adjust(2, 3, 1)

# Создаем клавиатуру
keybord_status = builder.as_markup(
    resize_keyboard=True, one_time_keyboard=True)
