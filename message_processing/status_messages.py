import psutil

from Funcs.state import return_message
from Funcs.status_commands import StatusCommands
from Funcs.task_proc import get_processes_running, list_to_string


class StatusMessage:

    @staticmethod
    async def status_komp(func: str):
        """
        Обрабатывает статус-команды.
        Функция АСИНХРОННАЯ, так как внутри вызывает await.
        """

        if func == "Батарея":
            battery = psutil.sensors_battery()

            # Проверка: есть ли вообще батарея (на ПК вернет None)
            if battery is None:
                return return_message("Батарея не обнаружена (возможно, это стационарный ПК).\n")

            percent = int(battery.percent)
            status_text = "Заряжается" if battery.power_plugged else "Не заряжается"

            text = f"Заряд батареи: {percent}%\n{status_text} "
            return return_message(text)

        elif func == 'Открытые программы':
            # Вызываем асинхронную функцию получения процессов
            lstp = await get_processes_running()

            # Ограничим вывод, иначе сообщение может быть слишком длинным для Telegram
            if len(lstp) > 50:
                lstp = lstp[:50]
                lstp.append("... (список обрезан)")

            # Используем list_to_string для форматирования списка
            # Добавляем перенос строки к каждому элементу
            formatted_list = [f"{p}\n" for p in lstp]
            programs_text = list_to_string(formatted_list)

            return return_message(f"Открытые программы:\n\n{programs_text}\n")

        elif func == "Закрыть программу":
            return return_message("Введите название программы для закрытия (например, chrome.exe):")

        elif func == "Логи":
            return return_message("Файл логов формируется и отправляется...")

        elif func == "Яркость":
            brightness_info = await StatusCommands.get_brightness()
            return return_message(f"{brightness_info}\nУкажите новый уровень яркости (0-100):\n")

        elif func == 'Звук':
            volume_level = await StatusCommands.get_sound_volume()
            return f"Уровень звука: {volume_level}\nВведите уровень звука, который нужно установить (или Max/Mute):"

        else:
            return return_message('Неправильная команда. Попробуйте выбрать другую\n')
