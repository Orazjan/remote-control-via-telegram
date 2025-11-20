from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Создаем билдер
builder = ReplyKeyboardBuilder()

# Добавляем кнопки
builder.button(text="Покинуть систему")
builder.button(text="Перезагрузка")
builder.button(text="Заблокировать экран")
builder.button(text="Завершение работы")

# Настраиваем сетку
builder.adjust(2)

# Создаем клавиатуру
keybord_komp = builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
