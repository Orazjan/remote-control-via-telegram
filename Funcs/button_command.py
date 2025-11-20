import asyncio

import pyautogui as pag


class ButtonCommands:
    """
    Класс для управления нажатиями клавиш.
    Все методы асинхронные, чтобы не блокировать бота.
    """

    @staticmethod
    async def close_alt():
        """Закрывает активное окно (Alt + F4)"""
        # Запускаем в отдельном потоке, чтобы бот не завис
        await asyncio.to_thread(pag.hotkey, 'alt', 'f4')

    @staticmethod
    async def alt_tab():
        """Переключает окно (Alt + Tab)"""
        await asyncio.to_thread(pag.hotkey, 'alt', 'tab')

    @staticmethod
    async def press_f5():
        """Обновляет страницу (F5)"""
        await asyncio.to_thread(pag.press, 'f5')
