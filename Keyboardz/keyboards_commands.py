from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Создаем билдер
builder = ReplyKeyboardBuilder()

# Добавляем кнопки
builder.button(text="ALT F4")
builder.button(text="ALT TAB")
builder.button(text="F5")

# Настраиваем сетку:
# 3 кнопки в одном ряду
builder.adjust(3)

# Создаем объект клавиатуры
keyboard_commands = builder.as_markup(
    resize_keyboard=True, one_time_keyboard=True)
