# notification

text for vbs file in autorun

Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "Path to awtorun.bat", 0, false

text for bat file

TIMEOUT /T 3
D:
RD /S /Q "path to folder where git project has been cloned"
TIMEOUT /T 3
cd "path to folder where git project has been cloned"
git clone https://github.com/Orazjan/notification.git 
TIMEOUT /T 3
Path to python.exe or write python if its in windows path Path to main.py from where git cloned project

