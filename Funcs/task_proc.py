import re

from subprocess import check_output

def get_processes_running():
    tasks = check_output(['tasklist']).decode('cp866', 'ignore').split("\r\n")
    p = []
    for task in tasks:
        m = re.match(b'(.*?)\\s+(\\d+)\\s+(\\w+)\\s+(\\w+)\\s+(.*?)\\s.*', task.encode())
        if m is not None:
            p.append(m.group(1).decode())
    return(p)

def list_to_string(text):
    str1 = ""
    for ele in text:
        str1 += ele
    return str1
