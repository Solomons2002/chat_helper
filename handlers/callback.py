from aiogram import types
from mics import dp , bot
from models import Database
import text
import markup
from re import compile
from aiogram.dispatcher.filters.builtin import CommandStart
import datetime
import config
from states import AddKey,UpdateText

db = Database()
@dp.callback_query_handler(lambda call : call.data[:8] == 'add_key_',  state = AddKey.state)
async def message(query ,  state):
    await bot.delete_message(
             chat_id = query.message.chat.id,
             message_id = query.message.message_id
        )    
    await query.message.answer(
            text = "ℹ️Добавляйте ключевые слова вот в такое формате :\n*коды запчастей* , *запчасти*\n▪️Главное чтобы до и после запятой стоял пробел.",
            reply_markup = markup.cancel,
            parse_mode = 'Markdown'
        )
    await state.update_data(name = query.data[8:])
    await AddKey.key.set()
    
    
@dp.message_handler(state = AddKey.key, text = '🚫 Отмена')
async def message( message, state):

    await message.answer(
            text = '*Главное меню*',
            reply_markup = markup.main_menu,
            parse_mode = 'Markdown'
        )    
    await state.finish()
    
@dp.message_handler(state = AddKey.key, content_types = types.ContentType.TEXT)
async def message( message, state):
    a = await state.get_data()
    for key in message.text.split(' , '):
       
        if len(message.text.split(' , ')) < 2:
           await db.add_key(a['name'], key )
           break

        else:
            await db.add_key(a['name'] , key 
            )
    await state.finish()
    await message.answer(
            text = '*Главное меню*',
            reply_markup = markup.main_menu,
            parse_mode = 'Markdown'
        )    
@dp.callback_query_handler(lambda call : call.data[:8] == 'del_key_')
async def message(query ,  state):
    lists = await db.get_keys(query.data[8:])
    await bot.edit_message_text(
             
             chat_id = query.message.chat.id,
             message_id = query.message.message_id,
             text = 'Выберите ключ который хотите удалить',
             reply_markup = markup.get_keys_markup(lists)
        )
@dp.callback_query_handler(lambda call : call.data[:9] == 'del2_key_')
async def message(query ,  state):
    await db.delete_key(query.data[9:])

    await bot.delete_message(
             chat_id = query.message.chat.id,
             message_id = query.message.message_id
        )
    await query.message.answer(
            text = '*Главное меню*',
            reply_markup = markup.main_menu,
            parse_mode = 'Markdown'
        )
        
@dp.callback_query_handler(lambda call : call.data[:8] == 'up_text_',  state = UpdateText.state)
async def message(query ,  state):
    await state.update_data(name = query.data[8:])
    await query.message.answer(
            text = "Введите новый текс для пары ключей",
            reply_markup = markup.cancel
        )
    await UpdateText.text.set()
    
