# import pyautogui as pag
# from aiogram import types
# from Handlers.handlers import dp, Dispatcher
# from Keyboardz.keyboard_call_back import get_keyboard

# user_data = {}

# @dp.message_handler(commands="control")
# async def csa(message: types.Message):
#     user_data[message.message_id] = 0
#     await message.answer("Укажите число: 0", reply_markup=get_keyboard())

# @dp.callback_query_handler(lambda c: c.data == user_data)
# async def callbacks_num(call: types.CallbackQuery):
#     # Получаем текущее значение для пользователя, либо считаем его равным 0
#     # Парсим строку и извлекаем действие, например `num_incr` -> `incr`
#     action = user_data.get(call.from_user.id, 0)
#     if action == "up":
#         pag.press("up")
#     elif action == "down":
#         pag.press("down")
#     if action == "left":
#         pag.press("down")
#     elif action == "right":
#         pag.press("right")
#     elif action == "end":
#         # Если бы мы не меняли сообщение, то можно было бы просто удалить клавиатуру
#         # вызовом await call.message.delete_reply_markup().
#         # Но т.к. мы редактируем сообщение и не отправляем новую клавиатуру,
#         # то она будет удалена и так.
#         await call.message.edit_text("Итого: получилось")
#     # Не забываем отчитаться о получении колбэка
#     await call.answer()
# """End call back"""
