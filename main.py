import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from environs import Env

import Funcs.state as st
from Funcs.status_commands import StatusCommands
from Handlers import (call_back_klawa, handlers, sound_handler, state_buttons,
                      state_command, state_fun, state_open, state_work)

# Читаем конфиг
env = Env()
env.read_env()

BOT_TOKEN = env.str('Api_Token')
ADMIN_ID = env.int('id')


async def setup_bot_commands(bot: Bot):
    """Регистрация команд в меню бота"""
    bot_commands = [
        types.BotCommand(command="/start", description="Начать/перезапустить"),
        types.BotCommand(command="/help", description="Что я умею?"),
        types.BotCommand(command="/rabota", description="Работа компьютера"),
        types.BotCommand(command="/zvuk", description="Громкость"),
        types.BotCommand(command="/status",
                         description="Состояние компьютера"),
        types.BotCommand(command="/comands", description="Кнопки действий"),
        types.BotCommand(command="/openweb", description="Открыть сайт"),
        types.BotCommand(command="/control", description="Управление"),
        types.BotCommand(command="/kill", description="Отключить программу"),
        types.BotCommand(command="/cancel", description="Отмена выключения")

    ]
    await bot.set_my_commands(bot_commands)


async def on_startup_notify(bot: Bot):
    """Действия при запуске: ставим время, включаем логи и шлем сообщение админу"""
    try:
        # Инициализация записи логов в файл
        StatusCommands.setup_logging()

        # Обновляем глобальную переменную времени (имя изменено на snake_case)
        st.start_time = st.get_current_time()

        # Получаем инфу о процессоре
        proc_info = handlers.get_proc()

        message_text = st.return_message(
            f"Компьютер \n{proc_info} \nвключён в ")

        # Устанавливаем меню команд
        await setup_bot_commands(bot)

        # Отправляем сообщение админу
        await bot.send_message(ADMIN_ID, message_text, reply_markup=types.ReplyKeyboardRemove())
        logging.info("Уведомление о запуске успешно отправлено.")

    except Exception as e:
        logging.error(f"Ошибка при отправке уведомления о старте: {e}")


async def main():
    # Базовое логирование в консоль
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )

    # Создание объектов
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    # Регистрируем роутеры
    dp.include_routers(
        handlers.router,         # Основные команды (/start, /help)
        state_work.router,       # /rabota
        sound_handler.router,    # /zvuk
        state_buttons.router,    # /comands
        state_command.router,    # /status
        state_open.router,       # /openweb
        state_fun.router,        # /funfun
        call_back_klawa.router   # /control (инлайн кнопки)
    )
    # Удаляем вебхук и сбрасываем апдейты (на всякий случай)
    await bot.delete_webhook(drop_pending_updates=True)

    # Запускаем логику старта (уведомление)
    await on_startup_notify(bot)

    try:
        print("Бот запущен! Нажмите Ctrl+C для выхода.")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
        print("Сессия бота закрыта.")

if __name__ == "__main__":
    try:
        # Запуск асинхронного цикла (кроссплатформенно)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен пользователем")
