from aiogram.utils import executor
import Handlers.handlers as HD
from aiogram import types
from Funcs.status_commands import status_Commands
from Handlers import state_work as SG, state_command as SC, state_open as SO, state_fun as SF, call_back_klawa as CB, state_buttons as SB

#####################################################
#                                                   #
#                                                   #
#№№№№№№№№№№№№№ Не забыть убрать ЛОГ #################
#                                                   #
#                                                   #
#####################################################

status_Commands.loggings()

HD.register_handler_client(HD.dp)
SG.register_handler_state_work(HD.dp)
SB.register_handler_state_button(HD.dp)
SC.register_handler_state_command(HD.dp)
SO.register_handler_state_open(HD.dp)
SF.register_handler_fun_command(HD.dp)
CB.register_handler_control(HD.dp)

executor.start(HD.dp, HD.on_startup())
executor.start_polling(HD.dp, skip_updates=True)
