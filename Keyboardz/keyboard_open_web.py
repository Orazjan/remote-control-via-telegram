from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Создаем билдер
builder = ReplyKeyboardBuilder()

# Добавляем кнопки
builder.button(text="Vk")
builder.button(text="YouTube")
builder.button(text="Закрыть окно")
builder.button(text="Открыть последнее окно")
builder.button(text="Другой сайт")

# Настраиваем сетку:
# 3 кнопки в первом ряду (Vk, YouTube, Закрыть)
# 2 кнопки во втором (Открыть последнее, Другой)
builder.adjust(3, 2)

# Создаем объект клавиатуры
keyboard_open = builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
