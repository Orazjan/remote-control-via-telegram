import Handlers.Handlers as HD
from aiogram.utils import executor
from Handlers.Funcs import Logging
from Handlers import StateWork as SG, StateCommand as SC, StateOpen as SO, StateFun as SF

Logging()

SG.register_Handler_StateWork(HD.dp)
SC.register_Handler_Statecommand(HD.dp)
SO.register_Handler_StateOpen(HD.dp)
SF.register_Handler_FunCommand(HD.dp)
HD.register_Handler_Client(HD.dp)

executor.start(HD.dp, HD.on_startup())
executor.start_polling(HD.dp, skip_updates=True)
