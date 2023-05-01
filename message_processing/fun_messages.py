from Funcs.state import return_message

class Funs_messages:
    def fun_segment(func):
        if (func == "Напечатать"):
            func ='Введите текст на англ\n'
            return return_message(func)

        elif (func=="Рандом с мышкой"):
            func ='Введите количество секунд:\n'
            return return_message(f"{func}")

        elif (func == "Вывод окна"):
            return return_message("Введите текст или выберите из меню:\n")

        elif func == 'Другое':
            return return_message("На данный момент данная функция не доступна, но мы работает над ней")

        elif func == "Нажать на кнопку":
            return "Введите кнопку, которую нужно нажать:"

        else:
            return return_message('Неправильная команда. Попробуйте выбрать другую\n')