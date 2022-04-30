import logging 
import os, random as rd
import pyautogui as pag
from Handlers import State, TaskProc, Handlers

path = "D://Projects/PY/ForBot/notification/screens/"

def Logging():
    Log_Format = "%(levelname)s %(asctime)s - %(message)s"

    logging.basicConfig(filename = f"{path}/logfile.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.ERROR)

    logger = logging.getLogger()
    logger.error(State.ReturnMessage(f"For check \n{Handlers.getproc()}"))
    logger.info(State.ReturnMessage(f"This is log file {Handlers.getproc()}"))

def ReadAndSendLogs():
    try:
        logfile = open(f'{path}/logfile.log')
    except :
        return "Ошибка нет файла"
        
    array =[]
    for p in logfile:
        array.append(p+"\n")

    return TaskProc.listToString(array)

def Cancel():
    os.system("shutdown -a")


def Shutdown():
    os.system(
        "shutdown -s -t 20 -c \"Сервер будет выключен через 20 секунд. Сохраните свои документы!\"")


def Reboot():
    os.system(
        "shutdown -r -t 20 -c \"Этот компьютер будет перезагружен через 20 секунд.\"")


def LeaveSession():
    os.system("shutdown -l")


def KillWind():
    pag.hotkey('ctrl', 'w' )


def KillProcess(text):
    os.system(f"taskkill /f /im {text}")


def KillFunc():
    os.system("taskkill /f /im python.exe")

def WriteText(text):
    pag.typewrite(f"{text}", interval=0.25)


def MouseRand(func):
    pag.FAILSAFE = False
    a = rd.randint(200, 1080)   # x
    b = rd.randint(300, 1080)   # y
    pag.moveTo(a, b, int(func))


def WindowWarning(func):
    pag.alert(func)


def Screenshot():
    pag.screenshot(f'{path}/ss.png')
    
