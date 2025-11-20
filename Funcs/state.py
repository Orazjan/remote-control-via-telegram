from datetime import datetime

# Переменная для хранения времени запуска
# Переименовал в snake_case. Не забудь поправить в main.py и handlers.py!
start_time = ""


def get_current_time():
    """Возвращает текущее время в формате ЧЧ:ММ:СС - ДД.ММ"""
    return datetime.now().strftime("%H:%M:%S - %d.%m")


def return_message(text: str):
    """Добавляет текущее время к тексту сообщения"""
    # Используем f-строку и добавляем разделитель (например, пробел или скобки)
    # Было: text + return_time() -> "Текст12:00"
    # Стало: "Текст [12:00]"
    return f"{text} [{get_current_time()}]"
