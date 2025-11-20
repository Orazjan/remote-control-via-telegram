import os
import sys

# Определяем путь к папке со скриншотами
# Используем abspath и добавляем разделитель в конце вручную,
# чтобы конкатенация строк (f'{PATH}file.png') работала корректно.
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# Поднимаемся на уровень выше (из Funcs в корень)
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
SCREENS_DIR = os.path.join(PROJECT_ROOT, 'screens')

# Создаем папку, если её нет (иначе скриншоты выдадут ошибку)
if not os.path.exists(SCREENS_DIR):
    os.makedirs(SCREENS_DIR)

# Добавляем разделитель в конце (/, \) для удобства конкатенации путей
PATH = os.path.join(SCREENS_DIR, '')


def cancel_shutdown():
    """Отмена запланированного выключения"""
    os.system("shutdown -a")


def kill_bot_process():
    """
    Убивает процесс Python. 
    Это жесткий способ остановить бота.
    """
    os.system("taskkill /f /im python.exe")
    # sys.exit() # Альтернативный способ, но менее надежный


def get_help_text():
    """Возвращает текст помощи"""
    text = (
        "Список команд:\n"
        "/start - Включение / проверка связи\n"
        "/rabota - Перезагрузка / выключение / блокировка\n"
        "/status - Громкость / яркость / процессы / логи\n"
        "/openweb - Открыть сайты\n"
        "/control - Виртуальная клавиатура\n"
        "/funfun - Скриншоты / камера / блокировка ввода\n"
        "/cancel - Отмена выключения\n"
        "/kill - Отключить бота"
    )
    return text
