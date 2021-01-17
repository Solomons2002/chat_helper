from aiogram import types
from mics import dp , bot
from models import Database
import text
import markup
from re import compile
from aiogram.dispatcher.filters.builtin import CommandStart
import datetime
import config

db = Database()
@dp.message_handler(CommandStart(), chat_id = config.admin)
async def welcome(message):

    await message.answer(
             text = text.start_message,
             reply_markup = markup.main_menu,
             parse_mode = 'Markdown'
        )
    await db.create_table()
    await db.create_table2()
    