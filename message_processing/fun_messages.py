from Funcs.state import return_message


class FunMessages:

    @staticmethod
    def fun_segment(action: str):
        """Возвращает текст ответа в зависимости от выбранного действия"""

        if action == "Напечатать":
            return return_message('Введите текст на англ\n')

        elif action == "Рандом с мышкой":
            return return_message('Введите количество секунд:\n')

        elif action == "Вывод окна":
            return return_message("Введите текст или выберите из меню:\n")

        elif action == 'Другое':
            return return_message("На данный момент данная функция не доступна, но мы работаем над ней")

        elif action == "Нажать на кнопку":
            return return_message("Введите кнопку, которую нужно нажать:")

        else:
            return return_message(f'{action}: неправильная команда. Попробуйте выбрать другую\n')
