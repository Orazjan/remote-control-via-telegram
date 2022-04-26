import Handlers.Handlers as HD
from aiogram.utils import executor
from Handlers import StateWork as SG, StateCommand as SC, StateOpen as SO, StateFun as SF


HD.register_Handler_Client(HD.dp)

executor.start(HD.dp, HD.on_startup())
executor.start_polling(HD.dp, skip_updates=True)
