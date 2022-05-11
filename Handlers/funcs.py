import logging
import os
import random as rd
import pyautogui as pag
import screen_brightness_control as sbc
from Handlers import state, task_proc, handlers
from moduleforsound.sound import Sound

PATH = os.path.abspath('./screen/')

"""Статус сегмент"""

def loggings():
    logging.basicConfig(level=logging.INFO)
    log_format = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename = f"{PATH}logfile.log",
                    filemode = "w",
                    format = log_format,
                    level = logging.ERROR)
    
    logger = logging.getLogger()
    logger.error(state.return_message(f"For check \n{handlers.get_proc()}"))
    logger.info(state.return_message(f"This is log file {handlers.get_proc()}"))

def read_and_send_logs():
    try:
        logfile = open(f'{PATH}logfile.log')
    except FileNotFoundError:
        return "Ошибка: Файл не найден"

    array =[]
    for text in logfile:
        array.append(text+"\n")

    return task_proc.list_to_string(array)

def kill_process(text):
    os.system(f"taskkill /f /im {text}")

def get_brightness():
    for monitor in sbc.list_monitors():
        return f"Название монитора: {monitor}\nУровень яркости: {sbc.get_brightness(display=monitor)}%\n"

def bright_monitor(procent):
    sbc.set_brightness(procent)

def volume(level):
    if level == "Max":
        Sound.volume_max()
    elif level == "Mute":
        Sound.mute()
    else:
        Sound.volume_set(int(level))

"""Опен сегмент"""

def kill_wind():
    pag.hotkey('ctrl', 'w' )

def open_last_wind():
    pag.hotkey('ctrl', 'shift', 't')

"""Хандлер сегмент"""

def cancel():
    os.system("shutdown -a")

def kill_func():
    os.system("taskkill /f /im python.exe")

"""Ворк сегмент"""

def shutdown(secondy):
    os.system(
        f"shutdown -s -t {secondy} -c \"Сервер будет выключен через {secondy} секунд. Сохраните свои документы!\"")

def reboot(secondy):
    os.system(
        f"shutdown -r -t {secondy} -c \"Этот компьютер будет перезагружен через {secondy} секунд.\"")

def leave_session():
    os.system("shutdown -l")

def lock_screen():
    os.system(f"{'%'}SystemRoot%/system32/rundll32.exe USER32.DLL LockWorkStation")

"""Фан сегмент"""

def write_text(text):
    pag.typewrite(f"{text}", interval=0.25)

def mouse_rand(func):
    pag.FAILSAFE = False
    value_for_x = rd.randint(200, 1080)   # x
    value_for_y = rd.randint(300, 1080)   # y
    pag.moveTo(value_for_x, value_for_y, int(func))

def window_warning(func):
    pag.alert(func)

def press_keyboard(text):
    pag.hotkey(f'{text}')

def screenshot():
    pag.screenshot(f'{PATH}ss.png')

"""Хендлер сегмент"""

def help():
    text = "Start - включение /проверка работает или нет\n"
    text += "Rabota - Перезагрузка /выключение /выйти из системы /заблокировать экран\n"
    text += "Status - батарея /яркость /звук /открытые программы /закрыть программу /логи\n"
    text += "Open_web - открыть вк /youtube /закрыть окно /открыть последнее окно\n"
    return text
