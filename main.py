import logging
import Handlers.Handlers as HD
from aiogram.utils import executor
from Handlers import StateWork as SG, StateCommand as SC, StateOpen as SO, StateFun as SF

logger = logging.getLogger()
handler = logging.FileHandler('D://Projects/PY/ForBot/logfile.log')
logger.addHandler(handler)
logger.error('This is log File')

SG.register_Handler_StateWork(HD.dp)
SC.register_Handler_Statecommand(HD.dp)
SO.register_Handler_StateOpen(HD.dp)
SF.register_Handler_FunCommand(HD.dp)
HD.register_Handler_Client(HD.dp)

executor.start(HD.dp, HD.on_startup())
executor.start_polling(HD.dp, skip_updates=True)
