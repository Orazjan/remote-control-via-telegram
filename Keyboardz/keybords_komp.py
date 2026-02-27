from aiogram.utils.keyboard import ReplyKeyboardBuilder

builder = ReplyKeyboardBuilder()

builder.button(text="Покинуть систему")
builder.button(text="Перезагрузка")
builder.button(text="Заблокировать экран")
builder.button(text="Завершение работы")
builder.button(text="Отмена выключения")

builder.adjust(2)

keybord_komp = builder.as_markup(resize_keyboard=True, one_time_keyboard=True)
