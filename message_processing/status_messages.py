from Funcs.task_proc import get_processes_running, list_to_string
import psutil
from Funcs import funcs
from Funcs.state import return_message
from Funcs import status_commands as sc

class status_message:

    def status_komp(func):
        if (func == "Батарея"):
            battery = psutil.sensors_battery()
            percent = int(battery.percent)
            if (battery.power_plugged == True):
                text = "Заряд батареи: " + str(percent) + "\nЗаряжается "
            else:
                text = "Заряд батареи: " + str(percent) + "\nНе заряжается "
            return return_message(text)

        elif (func == 'Открытые программы'):
            lstp = get_processes_running()
            array =[]
            for p in lstp:
                array.append(p+"\n")
            func = f"Открытые программы\n\n{list_to_string(array)}\n\n"
            return return_message(func)

        elif func == "Закрыть программу":
            return return_message("Закрыть программу")

        elif (func == "Логи"):
            return return_message(sc.status_Commands.read_and_send_logs())

        elif func == "Яркость":
            return return_message(f"{sc.status_Commands.get_brightness()}\nУкажите уровень яркости:\n")

        elif func == 'Звук':
            return (f"Уровень звука {sc.status_Commands.get_sound_volume()}\nВведите уровень звука, который нужно установить:")

        else:
            return return_message('Неправильная команда. Попробуйте выбрать другую\n')
