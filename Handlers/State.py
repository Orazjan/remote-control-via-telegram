import psutil
from Handlers import Funcs
import Handlers.Opens as op
from datetime import datetime
from Keyboardz.KeyboardFun import *
from Handlers.TaskProc import get_processes_running, listToString


def ReturnTime():
    dt = datetime.now()
    bt = dt.strftime("%H:%M:%S - %d.%m")
    return bt


def ReturnMessage(text):
    return text + ReturnTime()

def Workkomp(func):
    if (func == "Покинуть систему"):
        func = "Вы покинете систему через несколько секунд "
        Funcs.LeaveSession()
        return ReturnMessage(func)

    elif (func == "Перезагрузка"):
        func = "Компьютер перезагрузится через 20 секунд "
        Funcs.Reboot()
        return ReturnMessage(func)

    elif (func == "Завершение работы"):
        func = "Компьютер выключится через 20 секунд "
        Funcs.Shutdown()
        return ReturnMessage(func)
        
    else:
        return ReturnMessage('Неправильная команда. Попробуйте выбрать другую\n')

def FunSegment(func):
    if (func == "Напечатать"):
        func ='Введите текст на англ\n'
        return ReturnMessage(func)
    
    elif (func=="Рандом с мышкой"):
        func ='Введите количество секунд:\n'
        return ReturnMessage(f"{func}")

    elif (func == "Вывод окна"):
        return ReturnMessage("Введите текст или выберите из меню:\n")        

    elif (func == "Скриншот экрана"):
        return ReturnMessage("Скриншот готов ")

    else:
        return ReturnMessage('Неправильная команда. Попробуйте выбрать другую\n')

def StatusKomp(func):
    if (func == "Батарея"):
        battery = psutil.sensors_battery()
        percent = int(battery.percent)
        if (battery.power_plugged == True):
            text = "Заряд батареи: " + str(percent) + "\nЗаряжается "
            return ReturnMessage(text)
        else:
            text = "Заряд батареи: " + str(percent) + "\nНе заряжается "
            return ReturnMessage(text)
            
    elif (func == 'Открытые программы'):
        lstp = get_processes_running()
        array =[]
        for p in lstp:
            array.append(p+"\n")
        func = f"Открытые программы\n\n{listToString(array)}\n\n"
        return ReturnMessage(func)
    
    elif (func == "Закрыть окно"):
        Funcs.KillWind()
        return ReturnMessage("Окно закрыто ")

    else:
        return ReturnMessage('Неправильная команда. Попробуйте выбрать другую\n')


def OpenWeb(func):
    if (func == "Vk"):
        func = "Открывается ВК "
        op.openVK()

    elif (func == "YouTube"):
        func = "Открывается YouTube "
        op.openYoutube()

    elif (func == "Другой сайт"):
        func = "Введите ссылку на сайт: "
    
    else:
        return ReturnMessage('Неправильная команда. Попробуйте выбрать другую\n')
