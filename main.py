"""
    just Main
"""
from aiogram.utils import executor
import Handlers.handlers as HD
from Handlers.funcs import loggings
from Handlers import state_work as SG, state_command as SC, state_open as SO, state_fun as SF

loggings()

HD.register_handler_client(HD.dp)
SG.register_handler_state_work(HD.dp)
SC.register_handler_state_command(HD.dp)
SO.register_handler_state_open(HD.dp)
SF.register_handler_fun_command(HD.dp)

executor.start(HD.dp, HD.on_startup())
executor.start_polling(HD.dp, skip_updates=True)
