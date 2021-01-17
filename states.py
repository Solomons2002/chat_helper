from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from mics import dp , bot
from models import Database
from aiogram import types
import text
import markup
import datetime
import config


db = Database()
class CreatePairOfKeys(StatesGroup):
    name = State()
    keys = State()
    text = State()
    
class AddKey(StatesGroup):
    state = State()
    key = State()    
    
class UpdateText(StatesGroup):
    
    state = State()
    text = State()
        


    
@dp.message_handler(state = CreatePairOfKeys.name, text = '🚫 Отмена')
async def message( message, state):
    await message.answer(
            text = '*Главное меню*',
            reply_markup = markup.main_menu,
            parse_mode = 'Markdown'
        )    
    await state.finish()
    
@dp.message_handler(state = CreatePairOfKeys.name, content_types = types.ContentType.TEXT)
async def message( message, state):
    answer = await db.get_pair_of_key(message.text)
    print(answer)
    if  answer:
        await message.answer(
               'Данная пара ключей уже есть'
            )
        return
    else:
        await message.answer(
                text = 'Отлично \nℹ️Добавляйте ключевые слова вот в таком формате :\n*коды запчастей* , *запчасти*\n▪️Главное чтобы до и после запятой стоял пробел.",',
                parse_mode = 'Markdown'
            )    
    await state.update_data(name = message.text)
    await CreatePairOfKeys.keys.set()


@dp.message_handler(state = CreatePairOfKeys.keys, text = '🚫 Отмена')
async def message( message, state):
    await message.answer(
            text = '*Главное меню*',
            reply_markup = markup.main_menu,
            parse_mode = 'Markdown'
        )    
    await state.finish()
    
@dp.message_handler(state = CreatePairOfKeys.keys, content_types = types.ContentType.TEXT)
async def message( message, state):
    await message.answer(
            text = 'Отлично , теперь отправьте сообщение для ответа на ключи',
            parse_mode = 'Markdown'
            )    
    await state.update_data(keys = message.text)
    await CreatePairOfKeys.text.set() 


@dp.message_handler(state = CreatePairOfKeys.text, text = '🚫 Отмена')
async def message( message, state):
    await message.answer(
            text = '*Главное меню*',
            reply_markup = markup.main_menu,
            parse_mode = 'Markdown'
        )    
    await state.finish()
    
    
    
@dp.message_handler(state = CreatePairOfKeys.text, content_types = types.ContentType.TEXT)
async def message( message, state):
    await message.answer(
            text = 'Пара ключей настроена!',
            parse_mode = 'Markdown',
            reply_markup = markup.main_menu
            )    
    context = await state.get_data()
    await db.add_pair_of_keys( context['name'], message.text)
    for key in context['keys'].split(' , '):
       
        if len(context['keys'].split(' , ')) < 2:
           await db.add_key(context['name'], key )
           break

        else:
            await db.add_key(context['name'] , key )
        
    
    await state.finish()
    
@dp.message_handler(state = AddKey.state, content_types = types.ContentType.TEXT)
async def message( message, state): 
    await message.answer(
            text = '*Главное меню*',
            reply_markup = markup.main_menu,
            parse_mode = 'Markdown'
        )
    await state.finish()
    
@dp.message_handler(state = UpdateText.state, content_types = types.ContentType.TEXT)
async def message( message, state): 
    await message.answer(
            text = '*Главное меню*',
            reply_markup = markup.main_menu,
            parse_mode = 'Markdown'
        )
    await state.finish()
    
    
@dp.message_handler(state = UpdateText.text, text = '🚫 Отмена')
async def message( message, state):
    await message.answer(
            text = '*Главное меню*',
            reply_markup = markup.main_menu,
            parse_mode = 'Markdown'
        )    
    await state.finish()
    
@dp.message_handler(state = UpdateText.text, content_types = types.ContentType.TEXT)
async def message( message, state):
    answer = await state.get_data()
    await db.update_text(answer['name'], message.text)
    await message.answer(
            text = '*Главное меню*',
            reply_markup = markup.main_menu,
            parse_mode = 'Markdown'
        )    
    await state.finish()    