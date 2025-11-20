from Funcs.state import return_message
from Funcs.work_command import WorkCommands


class WorkMessages:

    @staticmethod
    async def work_komp(func: str):
        """
        Обрабатывает мгновенные действия (блокировка, выход).
        Для перезагрузки/выключения просто возвращает текст.
        """

        if func == "Покинуть систему":
            await WorkCommands.leave_session()
            return return_message("Вы покинете систему через несколько секунд ")

        elif func == "Заблокировать экран":
            await WorkCommands.lock_screen()
            return return_message('Компьютер заблокирован ')

        elif func == 'Перезагрузка' or func == 'Завершение работы':
            return return_message('Введите количество секунд: \n')

        else:
            return return_message('Неправильная команда. Попробуйте выбрать другую\n')

    @staticmethod
    async def perezagruzka(text: str, seconds: str):
        """
        Выполняет действие (выкл/перезагрузка) с таймером.
        """
        if text == 'Перезагрузка':
            await WorkCommands.reboot(seconds)
            return return_message(f"Компьютер будет перезагружен через {seconds} секунд\n")

        elif text == 'Завершение работы':
            await WorkCommands.shutdown(seconds)
            return return_message(f"Компьютер будет выключен через {seconds} секунд\n")

        else:
            return return_message('Неправильная команда. Попробуйте выбрать другую\n')
