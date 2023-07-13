from Funcs.state import return_message
from Funcs.button_command import buttons_commands


class button_messages:
    def button_segment(func):
        if (func == "ALT F4"):
            func = 'Вы нажали на ALT F4\n'
            buttons_commands.closealt()
            return return_message(func)

        elif (func == "ALT TAB"):
            func = 'Вы нажали на ALT TAB\n'
            buttons_commands.alttab()
            return return_message(f"{func}")

        elif (func == "F5"):
            func = "Вы нажали на F5\n"
            buttons_commands.F5()
            return return_message(func)

        else:
            return return_message(f'{func}: неправильная команда. Попробуйте выбрать другую\n')
