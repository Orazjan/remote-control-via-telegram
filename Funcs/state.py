from datetime import datetime
import psutil
from Funcs import funcs
from Funcs.task_proc import get_processes_running, list_to_string

startTime = ""

def return_time():
    d_t = datetime.now()
    b_t = d_t.strftime("%H:%M:%S - %d.%m")
    return b_t

def return_message(text):
    return text + return_time()

def work_komp(func):
    if func == "Покинуть систему":
        func = "Вы покинете систему через несколько секунд "
        funcs.leave_session()

    elif func == "Заблокировать экран":
        func = 'Компьютер заблокирован '
        funcs.lock_screen()
        return_message(func)

    elif func == 'Перезагрузка' or func == 'Завершение работы':
        return return_message('Введите количество секунд: \n')

    else:
        return return_message('Неправильная команда. Попробуйте выбрать другую\n')
    return return_message(func)

def perezagruzka(text, seconds):
    if text == 'Перезагрузка':
        funcs.reboot(seconds)
        return return_message(f"Компьютер будет перезагружен через {seconds} секунд\n")

    elif text == 'Завершение работы':
        funcs.shutdown(seconds)
        return return_message(f"Компьютер будет выключен через {seconds} секунд\n")
    else:
        return return_message('Неправильная команда. Попробуйте выбрать другую\n')

def fun_segment(func):
    if (func == "Напечатать"):
        func ='Введите текст на англ\n'
        return return_message(func)

    elif (func=="Рандом с мышкой"):
        func ='Введите количество секунд:\n'
        return return_message(f"{func}")

    elif (func == "Вывод окна"):
        return return_message("Введите текст или выберите из меню:\n")

    elif func == 'Другое':
        return return_message("На данный момент данная функция не доступна, но мы работает над ней")

    elif func == "Нажать на кнопку":
        return "Введите кнопку, которую нужно нажать:"

    else:
        return return_message('Неправильная команда. Попробуйте выбрать другую\n')

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
        return return_message(funcs.read_and_send_logs())

    elif func == "Яркость":
        return return_message(f"{funcs.get_brightness()}\nУкажите уровень яркости:\n")

    elif func == 'Звук':
        return (f"Уровень звука {funcs.get_sound_volume()}\nВведите уровень звука, который нужно установить:")

    else:
        return return_message('Неправильная команда. Попробуйте выбрать другую\n')

