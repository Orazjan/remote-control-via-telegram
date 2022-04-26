# notification

text for vbs file in autorun

Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "D:\Projects\PY\ForBot\Awturun.bat", 0, false
WshShell.Run "D:\Projects\PY\Horoscop_bot-main\Awturun.bat", 0, false

text for bat file

TIMEOUT /T 3
D:
RD /S /Q "D:\Projects\PY\ForBot\notification"
TIMEOUT /T 3
cd D:\Projects\PY\ForBot 
git clone https://github.com/Orazjan/notification.git 
TIMEOUT /T 3
C:\Users\Admin\AppData\Local\Programs\Python\Python310\python.exe D:\Projects\PY\ForBot\notification\main.py

