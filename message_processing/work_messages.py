from Funcs import work_command
from Funcs import funcs
from Funcs.state import return_message

class work_message:
    def work_komp(func):
        if func == "Покинуть систему":
            func = "Вы покинете систему через несколько секунд "
            work_command.work_commands.leave_session()

        elif func == "Заблокировать экран":
            func = 'Компьютер заблокирован '
            work_command.work_commands.lock_screen()
            return_message(func)

        elif func == 'Перезагрузка' or func == 'Завершение работы':
            return return_message('Введите количество секунд: \n')

        else:
            return return_message('Неправильная команда. Попробуйте выбрать другую\n')
        return return_message(func)

    def perezagruzka(text, seconds):
        if text == 'Перезагрузка':
            work_command.work_commands.reboot(seconds)
            return return_message(f"Компьютер будет перезагружен через {seconds} секунд\n")
    
        elif text == 'Завершение работы':
            work_command.work_commands.shutdown(seconds)
            return return_message(f"Компьютер будет выключен через {seconds} секунд\n")
        else:
            return return_message('Неправильная команда. Попробуйте выбрать другую\n')
