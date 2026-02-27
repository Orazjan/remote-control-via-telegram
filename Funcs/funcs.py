import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
SCREENS_DIR = os.path.join(PROJECT_ROOT, 'screens')

# Создаем папку, если её нет (иначе скриншоты выдадут ошибку)
if not os.path.exists(SCREENS_DIR):
    os.makedirs(SCREENS_DIR)

PATH = os.path.join(SCREENS_DIR, '')


def kill_bot_process():
    """
    Убивает процесс Python. 
    """
    os.system("taskkill /f /im python.exe")


def get_help_text():
    """Возвращает текст помощи"""
    text = (
        "Список команд:\n"
        "/start - Включение / проверка связи / отмена выключения\n"
        "/rabota - Перезагрузка / выключение / блокировка\n"
        "/status - Громкость / яркость / процессы / логи\n"
        "/openweb - Открыть сайты\n"
        "/control - Виртуальная клавиатура\n"
        "/kill - Отключить бота"
    )
    return text
