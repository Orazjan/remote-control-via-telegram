import asyncio
import os


class WorkCommands:
    """
    Класс команд управления питанием и сессией.
    Все методы асинхронные.
    """

    @staticmethod
    async def shutdown(seconds):
        """Выключение компьютера через N секунд"""
        try:
            # Приводим к int для безопасности (чтобы избежать инъекций команд)
            sec = int(seconds)
            comment = f"Сервер будет выключен через {sec} секунд. Сохраните свои документы!"

            # Формируем команду. В Windows кавычки для сообщения обязательны.
            cmd = f'shutdown -s -t {sec} -c "{comment}"'
            await asyncio.to_thread(os.system, cmd)
        except ValueError:
            print(f"Ошибка: Время '{seconds}' должно быть числом")

    @staticmethod
    async def reboot(seconds):
        """Перезагрузка компьютера через N секунд"""
        try:
            sec = int(seconds)
            comment = f"Этот компьютер будет перезагружен через {sec} секунд."

            cmd = f'shutdown -r -t {sec} -c "{comment}"'
            await asyncio.to_thread(os.system, cmd)
        except ValueError:
            print(f"Ошибка: Время '{seconds}' должно быть числом")

    @staticmethod
    async def leave_session():
        """Выход из учетной записи (Log off)"""
        await asyncio.to_thread(os.system, "shutdown -l")

    @staticmethod
    async def lock_screen():
        """Блокировка экрана (Win + L)"""
        # rundll32 обычно доступен в PATH, полный путь не обязателен,
        # но команда user32.dll,LockWorkStation (через запятую) стандартная.
        cmd = "rundll32.exe user32.dll,LockWorkStation"
        await asyncio.to_thread(os.system, cmd)
