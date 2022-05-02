import psutil
from Handlers import funcs
import Handlers.opens as op
from datetime import datetime
from Keyboardz.keyboard_fun import *
from Handlers.task_proc import get_processes_running, list_to_string


def return_time():
    dt = datetime.now()
    bt = dt.strftime("%H:%M:%S - %d.%m")
    return bt


def return_message(text):
    return text + return_time()

def work_komp(func):
    if (func == "Покинуть систему"):
        func = "Вы покинете систему через несколько секунд "
        funcs.leave_session()
        return return_message(func)

    elif (func == "Перезагрузка"):
        func = "Компьютер перезагрузится через 20 секунд "
        funcs.reboot()
        return return_message(func)

    elif (func == "Завершение работы"):
        func = "Компьютер выключится через 20 секунд "
        funcs.shutdown()
        return return_message(func)
        
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

    elif (func == "Скриншот экрана"):
        return return_message("Скриншот готов ")

    else:
        return return_message('Неправильная команда. Попробуйте выбрать другую\n')

def status_komp(func):
    if (func == "Батарея"):
        battery = psutil.sensors_battery()
        percent = int(battery.percent)
        if (battery.power_plugged == True):
            text = "Заряд батареи: " + str(percent) + "\nЗаряжается "
            return return_message(text)
        else:
            text = "Заряд батареи: " + str(percent) + "\nНе заряжается "
            return return_message(text)
            
    elif (func == "Закрыть окно"):
        funcs.kill_wind()
        return return_message("Окно закрыто ")

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
  
    else:
        return return_message('Неправильная команда. Попробуйте выбрать другую\n')


def open_web(func):
    if (func == "Vk"):
        func = "Открывается ВК "
        op.open_vk()

    elif (func == "YouTube"):
        func = "Открывается YouTube "
        op.open_youtube()

    elif (func == "Другой сайт"):
        func = "Введите ссылку на сайт: "
    
    else:
        return return_message('Неправильная команда. Попробуйте выбрать другую\n')
