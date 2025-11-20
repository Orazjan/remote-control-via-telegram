from Funcs.state import return_message
# Импортируем обновленный класс (убедись, что в button_command.py класс называется ButtonCommands)
from Funcs.button_command import ButtonCommands


class ButtonMessages:

    @staticmethod
    async def button_segment(command_text: str):
        """
        Обрабатывает текст кнопки и выполняет действие.
        Возвращает текст ответа для пользователя.
        """
        if command_text == "ALT F4":
            # Вызываем асинхронный метод
            await ButtonCommands.close_alt()
            return return_message('Вы нажали на ALT F4\n')

        elif command_text == "ALT TAB":
            await ButtonCommands.alt_tab()
            return return_message('Вы нажали на ALT TAB\n')

        elif command_text == "F5":
            await ButtonCommands.press_f5()
            return return_message("Вы нажали на F5\n")

        else:
            return return_message(f'{command_text}: неправильная команда. Попробуйте выбрать другую\n')
