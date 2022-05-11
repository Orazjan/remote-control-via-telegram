from aiogram import types
def get_keyboard():
    # Генерация клавиатуры.
    buttons = [
        types.InlineKeyboardButton(text="up", callback_data="kb_up"),
        types.InlineKeyboardButton(text="down", callback_data="kb_down"),
        types.InlineKeyboardButton(text="left", callback_data="kb_left"),
        types.InlineKeyboardButton(text="right", callback_data="kb_right"),
        types.InlineKeyboardButton(text="Закончить", callback_data="kb_end")
    ]
    # Благодаря row_width=2, в первом ряду будет две кнопки, а оставшаяся одна
    # уйдёт на следующую строку
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(buttons[0]).add(buttons[2], buttons[3]).add(buttons[1]).add(buttons[4])
    return keyboard
