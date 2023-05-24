import webbrowser
import pyautogui as pag


class openingUrl:
    def open_vk():
        webbrowser.open_new('https://vk.com')

    def open_youtube():
        webbrowser.open_new('https://youtube.com')

    def open_web(text):
        webbrowser.open_new(f'{text}')

    def kill_wind():
        pag.hotkey('ctrl', 'w')

    def open_last_wind():
        pag.hotkey('ctrl', 'shift', 't')
