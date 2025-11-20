# Импортируем обновленные команды
import Funcs.BrowserCommands as op
from Funcs.state import return_message


async def open_web(func: str):
    """
    Выполняет действие открытия сайта и возвращает сообщение.
    Теперь функция асинхронная!
    """
    if func == "Vk":
        await op.BrowserCommands.open_vk()
        return return_message("Открывается ВК ")

    elif func == "YouTube":
        await op.BrowserCommands.open_youtube()
        return return_message("Открывается YouTube ")

    elif func == "Открыть последнее окно":
        # В opens_commands мы переименовали open_last_wind -> restore_tab
        await op.BrowserCommands.restore_tab()
        return return_message("Последнее окно открыто\n")

    elif func == "Закрыть окно":
        # В opens_commands мы переименовали kill_wind -> close_tab
        await op.BrowserCommands.close_tab()
        return return_message("Окно закрыто ")

    elif func == "Другой сайт":
        # Тут действий нет, просто возвращаем текст
        return return_message("Введите ссылку на сайт:\n")

    else:
        return return_message('Неправильная команда. Попробуйте выбрать другую\n')
