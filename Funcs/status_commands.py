import logging
import os
import screen_brightness_control as sbc
from moduleforsound.sound import Sound
from Funcs import state, task_proc
from Funcs import funcs
from Handlers import handlers


class status_Commands:

    def loggings():
        log_format = "%(levelname)s %(asctime)s - %(message)s"
        logging.basicConfig(filename=f"{funcs.PATH}logfile.log",
                            filemode="w",
                            format=log_format,
                            level=logging.ERROR)

        logger = logging.getLogger()
        logger.error(state.return_message(
            f"For check \n{handlers.get_proc()}"))
        logger.info(state.return_message(
            f"This is log file {handlers.get_proc()}"))

    def read_and_send_logs():
        try:
            logfile = open(f'{funcs.PATH}logfile.log')
        except FileNotFoundError:
            return "Ошибка: Файл не найден"

        array = []
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

    def get_sound_volume():
        return Sound.current_volume()

    def volume(level):
        if level == "Max":
            Sound.volume_max()
        elif level == "Mute":
            Sound.mute()
        else:
            Sound.volume_set(int(level))
