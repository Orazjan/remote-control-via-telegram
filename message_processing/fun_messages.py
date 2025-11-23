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

        elif action == "Получить буфер обмена":
            return return_message("Текст из буфера обмена:\n")

        elif action == "Записать в буфер обмена":
            return return_message("Напишите текст, который нужно записать в буфер обмена:")

        elif action == "Записать звук":
            return return_message("Введите длительность записи в секундах:\n")

        else:
            return return_message(f'{action}: неправильная команда. Попробуйте выбрать другую\n')
