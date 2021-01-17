from aiogram import executor
from mics import dp, bot

import asyncio
import handlers


       


if __name__ == "__main__":
    #dp.loop.create_task(main(rows = 20 ,  params = 'OUT'))
    executor.start_polling(dp, skip_updates=True)