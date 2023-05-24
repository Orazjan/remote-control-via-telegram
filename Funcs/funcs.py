import os
import pyautogui as pag
from Handlers import handlers

PATH = os.path.abspath('./screens/')


def cancel():
    os.system("shutdown -a")


def kill_func():
    os.system("taskkill /f /im python.exe")


def help():
    text = "Start - включение /проверка работает или нет\n"
    text += "Rabota - Перезагрузка /выключение /выйти из системы /заблокировать экран\n"
    text += "Status - батарея /яркость /звук /открытые программы /закрыть программу /логи\n"
    text += "Open_web - открыть вк /youtube /закрыть окно /открыть последнее окно\n"
    return text
