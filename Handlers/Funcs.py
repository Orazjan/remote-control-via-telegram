import logging 
import os
import random as rd
import pyautogui as pag
from Handlers import state, task_proc, handlers

PATH = "D://Projects/PY/ForBot/notification/screens/"

def loggings():
    
    Log_Format = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename = f"{PATH}/logfile.log",
                    filemode = "w",
                    format = Log_Format, 
                    level = logging.ERROR)

    logger = logging.getLogger()
    logger.error(state.return_message(f"For check \n{handlers.get_proc()}"))
    logger.info(state.return_message(f"This is log file {handlers.get_proc()}"))

def read_and_send_logs():
    try:
        logfile = open(f'{PATH}/logfile.log')
    except :
        return "Ошибка нет файла"
        
    array =[]
    for p in logfile:
        array.append(p+"\n")

    return task_proc.list_to_string(array)

def cancel():
    os.system("shutdown -a")


def shutdown():
    os.system(
        "shutdown -s -t 20 -c \"Сервер будет выключен через 20 секунд. Сохраните свои документы!\"")


def reboot():
    os.system(
        "shutdown -r -t 20 -c \"Этот компьютер будет перезагружен через 20 секунд.\"")


def leave_session():
    os.system("shutdown -l")


def kill_wind():
    pag.hotkey('ctrl', 'w' )


def kill_process(text):
    os.system(f"taskkill /f /im {text}")


def kill_func():
    os.system("taskkill /f /im python.exe")

def write_text(text):
    pag.typewrite(f"{text}", interval=0.25)


def mouse_rand(func):
    pag.FAILSAFE = False
    a = rd.randint(200, 1080)   # x
    b = rd.randint(300, 1080)   # y
    pag.moveTo(a, b, int(func))


def window_warning(func):
    pag.alert(func)


def screenshot():
    pag.screenshot(f'{PATH}/ss.png')
    
