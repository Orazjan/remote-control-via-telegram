import Funcs.opens as op
from Funcs.state import return_message

def open_web(func):
    if (func == "Vk"):
        func = "Открывается ВК "
        op.openingUrl.open_vk()
        return return_message(func + " ")

    elif (func == "YouTube"):
        func = "Открывается YouTube "
        op.openingUrl.open_youtube()
        return return_message(func + " ")

    elif (func == "Открыть последнее окно"):
        op.openingUrl.open_last_wind()
        return return_message("Последнее окно открыто\n")

    elif (func == "Закрыть окно"):
        op.openingUrl.kill_wind()
        return return_message("Окно закрыто ")

    elif (func == "Другой сайт"):
        return return_message("Введите ссылку на сайт:\n")

    else:
        return return_message('Неправильная команда. Попробуйте выбрать другую\n')
