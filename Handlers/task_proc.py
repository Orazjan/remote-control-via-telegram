import re

from subprocess import check_output

def get_processes_running():
    """
    Takes tasklist output and parses the table into a dict
    """
    tasks = check_output(['tasklist']).decode('cp866', 'ignore').split("\r\n")
    p = []
    for task in tasks:
        m = re.match(b'(.*?)\\s+(\\d+)\\s+(\\w+)\\s+(\\w+)\\s+(.*?)\\s.*', task.encode())
        if m is not None:
            p.append(m.group(1).decode())
    return(p)

def list_to_string(s):
    str1 = "" 
    
    for ele in s: 
        str1 += ele  
    
    return str1 
