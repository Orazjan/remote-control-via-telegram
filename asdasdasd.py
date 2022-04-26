from datetime import datetime
import random as rd
import pyautogui as pag


# text = 'hren'
# pag.typewrite(f"{text}")    Тут можно ввести текст

# pag.typewrite('Hello world!', interval=0.25)  Тут используется интервал

# a = rd.randint(100, 680)
# print (a)
# b = rd.randint(100, 680)
# print (b)

# pag.moveTo(a, b, 10)
# pag.scroll(-60)

# print(pag.position())
# pag.alert("Программа перестала отвечать!\nПерезагрузите компьютер!")

# pag.hotkey('ctrl', 'w' )
dt = datetime.now()
bt = dt.strftime("%H %M %S")

scree_shot = pag.screenshot() # to store a PIL object containing the image in a variable
pag.screenshot(f'{bt}.png')
