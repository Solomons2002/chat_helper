import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import config 
import asyncio


bot = Bot(config.tg_token)

dp = Dispatcher(bot, asyncio.get_event_loop(), storage = MemoryStorage() )
logging.basicConfig(level=logging.INFO)