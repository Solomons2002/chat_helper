from aiogram import types
from mics import dp , bot
from models import Database
import text
import markup
from re import compile
from aiogram.dispatcher.filters.builtin import CommandStart
import datetime
import config
from states import CreatePairOfKeys, AddKey,UpdateText

db = Database()
@dp.message_handler(text = "🛠 Создать пару ключей")
async def message(message):
    await message.answer(
            text = text.create_pair_of_keys,
            reply_markup = markup.cancel,
            parse_mode = 'Markdown'
        )
    await CreatePairOfKeys.name.set()

@dp.message_handler(text = "➕ Добавить ключи')
async def message(message):
    lists = await db.get_all_pair_keys()
    print(lists)
    await message.answer(
            text = text.add_key_message,
            reply_markup = markup.get_all_pair_markup(lists),
            parse_mode = 'Markdown'
        )
    await AddKey.state.set()
   
   
@dp.message_handler(text = '❌ Удалить ключ')
async def message(message):
    lists = await db.get_all_pair_keys()
    print(lists)
    await message.answer(
            text = 'Выберете пару ключей',
            reply_markup = markup.get_all_pair_markup_del(lists),
            parse_mode = 'Markdown'
        )

@dp.message_handler(text = "💱 Изменить текст")
async def message(message):
    lists = await db.get_all_pair_keys()
    print(lists)
    await message.answer(
            text = 'Выберете пару ключей',
            reply_markup = markup.get_all_pair_markup_text(lists),
            parse_mode = 'Markdown'
        )
    await UpdateText.state.set()
    