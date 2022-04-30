import logging 
import os, random as rd
import pyautogui as pag
from Handlers import State

def Logging():
    Log_Format = "%(levelname)s %(asctime)s - %(message)s"

    logging.basicConfig(filename = "D://Projects/PY/ForBot/logfile.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.ERROR)

    logger = logging.getLogger()
    logger.info(State.ReturnMessage("This is log file "))

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
    pag.screenshot('D://Projects/PY/ForBot/screens/ss.png')
    
