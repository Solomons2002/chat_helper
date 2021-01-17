from aiogram import types
from mics import dp , bot
from models import Database
import text
import markup
import re
import datetime
import config

db = Database()
@dp.message_handler()
async def message(m):
    print(m)
    keys = await db.get_all_keys()
    for key in keys:
     
       if re.search(r'\b{}\b'.format(key['key']),m.text.lower()):
          text_key = await db.get_text(key['pair_of_keys'])

          await m.reply(
                  text = text_key
                 ) 
          return 
    '''
    
    print(m.text)
    messages = m.text.split(' ')
    for world in messages:
        print(world)
        ans = await db.get_keys_for_key(world)
        if ans:
            text_key = await db.get_text(ans)
            await m.reply(
                  text = text_key
                 )
            return'''
 