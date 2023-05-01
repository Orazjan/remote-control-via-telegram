import os

class work_commands:
    def shutdown(secondy):
        os.system(
            f"shutdown -s -t {secondy} -c \"Сервер будет выключен через {secondy} секунд. Сохраните свои документы!\"")


    def reboot(secondy):
        os.system(
            f"shutdown -r -t {secondy} -c \"Этот компьютер будет перезагружен через {secondy} секунд.\"")


    def leave_session():
        os.system("shutdown -l")


    def lock_screen():
        os.system(
            f"{'%'}SystemRoot%/system32/rundll32.exe USER32.DLL LockWorkStation")

