import re
import asyncio
from subprocess import check_output


async def get_processes_running():
    """
    Получает список запущенных процессов асинхронно.
    Возвращает список имен процессов.
    """
    try:
        # Запускаем subprocess в отдельном потоке, чтобы не блокировать бота
        output = await asyncio.to_thread(check_output, ['tasklist'])

        # Декодируем вывод (cp866 для русской Windows, иначе 'utf-8' или 'cp1251')
        # ignore нужен, чтобы не упало на странных символах
        decoded_output = output.decode('cp866', 'ignore')

        tasks = decoded_output.split("\r\n")
        p = []

        # Регулярка для строки (не байт).
        pattern = re.compile(r'(.*?)\s+(\d+)\s+(\w+)\s+(\w+)\s+(.*?)\s.*')

        for task in tasks:
            # Пропускаем пустые строки
            if not task:
                continue

            m = pattern.match(task)
            if m:
                p.append(m.group(1))

        return p

    except Exception as e:
        return [f"Ошибка получения процессов: {e}"]


def list_to_string(text_list):
    """
    Преобразует список строк в одну большую строку.
    В Python это делается через join.
    """
    return "".join(text_list)
