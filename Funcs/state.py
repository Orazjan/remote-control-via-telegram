from datetime import datetime

startTime = ""


def return_time():
    d_t = datetime.now()
    b_t = d_t.strftime("%H:%M:%S - %d.%m")
    return b_t


def return_message(text):
    return text + return_time()
