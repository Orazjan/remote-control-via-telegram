import logging
import os
import random as rd
import threading
import time
import asyncio
import pyperclip

import cv2
import pyautogui as pag

# Импортируем путьы из funcs
from Funcs import funcs

# Настраиваем логгер для этого файла
logger = logging.getLogger(__name__)


class FunFuncs:

    # Флаг для блокировки ввода
    _blocking_active = False

    @staticmethod
    def mouse_rand(duration):
        """
        Двигает мышь в случайную точку.
        """
        pag.FAILSAFE = False
        screen_width, screen_height = pag.size()

        value_for_x = rd.randint(0, screen_width - 1)
        value_for_y = rd.randint(0, screen_height - 1)

        try:
            pag.moveTo(value_for_x, value_for_y, duration=float(duration))
        except Exception as e:
            logger.error(f"Ошибка при движении мыши: {e}")

    @staticmethod
    def window_warning(message):
        """
        Выводит окно с предупреждением.
        Запускается в отдельном потоке, чтобы бот НЕ ждал, пока юзер нажмет ОК.
        """
        def show_alert():
            pag.alert(text=message, title="Warning from Bot")

        # Запускаем алерт параллельно
        threading.Thread(target=show_alert, daemon=True).start()

    @staticmethod
    def _blocking_process():
        """Внутренний метод цикла блокировки"""
        pag.FAILSAFE = False
        screen_w, screen_h = pag.size()

        # Пока флаг True, держим мышь в центре
        while FunFuncs._blocking_active:
            pag.moveTo(screen_w // 2, screen_h // 2)
            # Чуть уменьшил задержку для более жесткой блокировки
            time.sleep(0.05)

    @staticmethod
    def block_input(enable: bool):
        """Включает или выключает удержание мыши в центре"""
        if enable:
            if FunFuncs._blocking_active:
                return

            FunFuncs._blocking_active = True
            t = threading.Thread(
                target=FunFuncs._blocking_process, daemon=True)
            t.start()
        else:
            FunFuncs._blocking_active = False

    @staticmethod
    def screenshot():
        """Делает скриншот и сохраняет по пути из funcs.PATH"""
        try:
            # Убедимся, что папка существует
            save_path = f'{funcs.PATH}ss.png'
            os.makedirs(os.path.dirname(save_path), exist_ok=True)

            pag.screenshot(save_path)
        except Exception as e:
            logger.error(f"Ошибка создания скриншота: {e}")

    @staticmethod
    def get_photo_from_camera():
        """Делает фото с веб-камеры"""
        cap = None
        try:
            # 0 - индекс камеры по умолчанию
            cap = cv2.VideoCapture(0)

            if not cap.isOpened():
                logger.warning("Не удалось открыть камеру")
                return

            # Прогрев камеры (баланс белого, экспозиция)
            for _ in range(10):
                cap.read()

            ret, frame = cap.read()
            if ret:
                save_path = f'{funcs.PATH}cam.png'
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                cv2.imwrite(save_path, frame)
            else:
                logger.warning("Не удалось получить кадр с камеры")

        except Exception as e:
            logger.error(f"Ошибка камеры: {e}")
        finally:
            # Обязательно освобождаем ресурсы, даже если была ошибка
            if cap:
                cap.release()

    # Асинхронные методы для работы с буфером обмена
    @staticmethod
    async def get_clipboard():
        return await asyncio.to_thread(pyperclip.paste)

    @staticmethod
    async def set_clipboard(text: str):
        await asyncio.to_thread(pyperclip.copy, text)
