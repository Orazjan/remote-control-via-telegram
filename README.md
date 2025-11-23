🖥️ Remote Control via Telegram Bot

[English] | Русский

A powerful, asynchronous Telegram bot for remote computer administration and monitoring. Built with Python 3.10+ and Aiogram 3.x.

🚀 Features

System Control: Shutdown, Reboot, Lock Screen, Log off.

Monitoring: Battery status, running processes, screen brightness.

Media Control: Volume mixer per application, media keys (Play/Pause), brightness control.

Spying & Security: Webcam photos, screenshots, microphone recording, clipboard management.

Browser: Open URLs remotely, close/restore tabs.

Input Control: Block mouse/keyboard, virtual keyboard inputs.

🛠 Installation

Clone the repository:

git clone [https://github.com/Orazjan/remote-control-via-telegram.git](https://github.com/Orazjan/remote-control-via-telegram.git)
cd remote-control-via-telegram


Install dependencies:

pip install -r requirements.txt


(Key libs: aiogram, pyautogui, opencv-python, pycaw, sounddevice, screen-brightness-control, environs)

Configuration:
Create a .env file in the root directory:

Api_Token=YOUR_TELEGRAM_BOT_TOKEN
id=YOUR_TELEGRAM_ID
kompfirst=MyComputerName


Run:

python main.py


🎮 Commands List

Command

Description

/start

Check connection and view PC name.

/help

List of available commands.

/rabota

Power Menu: Shutdown, Reboot, Lock screen.

/status

System Info: Battery, running processes (tasklist), kill process, get logs.

/zvuk

Audio Mixer: Adjust volume for specific apps (e.g., mute Chrome, boost Spotify).

/control

Remote Input: Virtual keyboard arrows, Enter, Play/Pause.

/openweb

Browser: Open specific sites (VK, YouTube), close tabs.

/cancel

Cancel scheduled shutdown/reboot.

/kill

Stop the bot process remotely.

🤫 Secret Menu

The bot features a hidden command /funfun that is not listed in the main Telegram menu. This menu contains sensitive or "prank" features intended strictly for the administrator.

/funfun capabilities:

📸 Screenshot: Get a snapshot of the current screen.

📷 Webcam: Take a photo from the PC's webcam.

🎤 Record Audio: Record audio for N seconds.

📋 Clipboard: Read the current PC clipboard or send text to it.

🔒 Block Input: Completely block the mouse and keyboard.

🖱️ Random Mouse: Move the mouse cursor randomly (prank).

💬 Window Message: Show a popup alert window on the PC.

<a name="russian"></a>🇷🇺 Удаленное управление через Telegram

Мощный асинхронный Telegram-бот для удаленного администрирования и мониторинга компьютера. Написан на Python 3.10+ с использованием Aiogram 3.x.

🚀 Возможности

Управление питанием: Выключение, Перезагрузка, Блокировка экрана, Выход из системы.

Мониторинг: Заряд батареи, список процессов, яркость экрана.

Медиа: Микшер громкости для каждого приложения отдельно, управление яркостью.

Безопасность и Слежение: Фото с веб-камеры, скриншоты, прослушка микрофона, управление буфером обмена.

Браузер: Открытие ссылок, закрытие и восстановление вкладок.

Управление вводом: Блокировка мыши/клавиатуры, виртуальное нажатие клавиш.

🛠 Установка

Скачайте проект:

git clone [https://github.com/Orazjan/remote-control-via-telegram.git](https://github.com/Orazjan/remote-control-via-telegram.git)
cd remote-control-via-telegram


Установите библиотеки:

pip install -r requirements.txt


(Основные библиотеки: aiogram, pyautogui, opencv-python, pycaw, sounddevice, screen-brightness-control, environs)

Настройка:
Создайте файл .env в папке с проектом:

Api_Token=ВАШ_ТОКЕН_БОТА
id=ВАШ_TELEGRAM_ID
kompfirst=ИмяКомпьютера


Запуск:

python main.py


🎮 Список команд

Команда

Описание

/start

Проверка связи и имени ПК.

/help

Список доступных команд.

/rabota

Питание: Выключение, Перезагрузка, Блокировка, Выход.

/status

Статус: Батарея, список процессов, убить процесс, получить логи.

/zvuk

Аудио Микшер: Настройка громкости для конкретных программ.

/control

Управление: Виртуальные стрелочки, Enter, Пауза.

/openweb

Браузер: Открытие сайтов (VK, YouTube), управление вкладками.

/cancel

Отмена запланированного выключения.

/kill

Отключение самого бота.

🤫 Секретное меню

Бот содержит скрытую команду /funfun, которая не отображается в меню Telegram по умолчанию. Это меню содержит функции для слежения и взаимодействия, предназначенные только для владельца ПК.

Возможности /funfun:

📸 Скриншот: Получить снимок экрана.

📷 Веб-камера: Сделать скрытое фото с камеры.

🎤 Запись аудио: Записывает аудио в N секунд.

📋 Буфер обмена: Прочитать или записать текст в буфер обмена ПК.

🔒 Блокировка: Полностью заблокировать мышь и клавиатуру.

🖱️ Рандом мышь: Хаотичное движение курсора (пранк).

💬 Вывод окна: Вывести окно с сообщением на экран ПК.