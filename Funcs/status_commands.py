import logging
import os
import platform
import asyncio
import screen_brightness_control as sbc

# Пытаемся импортировать модуль звука.
# Если его нет или он работает с ошибками, бот не упадет при запуске.
try:
    from moduleforsound.sound import Sound
except ImportError:
    logging.warning(
        "Модуль moduleforsound не найден. Управление звуком будет недоступно.")
    Sound = None

from Funcs import state
from Funcs import funcs
# Убрали импорт task_proc, если он использовался только для логов (которые мы теперь шлем файлом)
# from Funcs import task_proc

# Получаем логгер
logger = logging.getLogger(__name__)


class StatusCommands:

    @staticmethod
    def setup_logging():
        """Настраивает запись логов в файл отдельно от консоли"""
        log_path = f"{funcs.PATH}logfile.log"

        # Создаем форматтер и обработчик файла
        file_formatter = logging.Formatter(
            "%(levelname)s %(asctime)s - %(message)s")
        file_handler = logging.FileHandler(
            log_path, mode="w", encoding='utf-8')
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.INFO)  # или ERROR, как тебе удобнее

        # Добавляем обработчик к корневому логгеру
        root_logger = logging.getLogger()
        root_logger.addHandler(file_handler)

        # Записываем стартовую инфу
        proc_info = platform.processor()
        root_logger.info(state.return_message(
            f"Log file initialized. Processor: {proc_info}"))

    @staticmethod
    async def kill_process(process_name: str):
        """Убивает процесс по имени"""
        # os.system блокирует поток, используем to_thread
        await asyncio.to_thread(os.system, f"taskkill /f /im {process_name}")

    @staticmethod
    async def get_brightness():
        """Получает яркость мониторов"""
        try:
            # sbc может тупить на некоторых мониторах, оборачиваем
            monitors = await asyncio.to_thread(sbc.list_monitors)

            if not monitors:
                return "Мониторы не найдены или не поддерживают управление."

            result = ""
            for monitor in monitors:
                # Получаем яркость
                # get_brightness возвращает список [50], берем первый элемент
                b_level = await asyncio.to_thread(sbc.get_brightness, display=monitor)
                val = b_level[0] if isinstance(b_level, list) else b_level
                result += f"Монитор: {monitor}\nЯркость: {val}%\n"
            return result

        except Exception as e:
            logger.error(f"Ошибка получения яркости: {e}")
            return "Не удалось получить данные о яркости."

    @staticmethod
    async def bright_monitor(percent):
        """Устанавливает яркость"""
        try:
            await asyncio.to_thread(sbc.set_brightness, int(percent))
        except Exception as e:
            logger.error(f"Ошибка установки яркости: {e}")

    @staticmethod
    async def get_sound_volume():
        if Sound:
            # Если библиотека синхронная, лучше обернуть
            vol = await asyncio.to_thread(Sound.current_volume)
            return vol
        return "Модуль звука отключен"

    @staticmethod
    async def volume(level):
        if not Sound:
            return

        try:
            if level == "Max":
                await asyncio.to_thread(Sound.volume_max)
            elif level == "Mute":
                await asyncio.to_thread(Sound.mute)
            else:
                await asyncio.to_thread(Sound.volume_set, int(level))
        except Exception as e:
            logger.error(f"Ошибка звука: {e}")
