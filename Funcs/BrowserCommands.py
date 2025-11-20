import webbrowser
import asyncio
import pyautogui as pag


class BrowserCommands:
    """
    Класс для управления браузером.
    Методы асинхронные для плавности работы бота.
    """

    @staticmethod
    async def open_vk():
        await asyncio.to_thread(webbrowser.open_new, 'https://vk.com')

    @staticmethod
    async def open_youtube():
        await asyncio.to_thread(webbrowser.open_new, 'https://youtube.com')

    @staticmethod
    async def open_web(url: str):
        """Открывает ссылку. Добавляет https, если его нет."""
        if not url.startswith(('http://', 'https://')):
            url = f'https://{url}'

        await asyncio.to_thread(webbrowser.open_new, url)

    @staticmethod
    async def close_tab():  # Бывшая kill_wind
        """Закрывает текущую вкладку (Ctrl + W)"""
        await asyncio.to_thread(pag.hotkey, 'ctrl', 'w')

    @staticmethod
    async def restore_tab():  # Бывшая open_last_wind
        """Восстанавливает закрытую вкладку (Ctrl + Shift + T)"""
        await asyncio.to_thread(pag.hotkey, 'ctrl', 'shift', 't')
