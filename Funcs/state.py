from datetime import datetime

# Переменная для хранения времени запуска
start_time = ""


def get_current_time():
    """Возвращает текущее время в формате ЧЧ:ММ:СС - ДД.ММ"""
    return datetime.now().strftime("%H:%M:%S - %d.%m")


def return_message(text: str):
    """Добавляет текущее время к тексту сообщения"""

    return f"{text} {get_current_time()}"
