import asyncpg
import asyncio
from mics import dp
import config
import datetime


import asyncio
import asyncpg
async def create_pool():       
    return await asyncpg.create_pool(
                user= 'Future',
                password = '123',
                database = 'Future',
                host = '127.0.0.1'

                )
            
            
    

db = dp.loop.run_until_complete(create_pool())

class Database:
    pool = db
    
    async def create_table(self):
        sql = '''create table if not exists pair_of_keys (
        name text,
        message text)
        '''
        async with self.pool.acquire() as connect:
            select = await connect.execute(sql)
            
    async def create_table2(self):
        sql = '''create table if not exists keys(
        pair_of_keys text,
        key text)
        
        '''        
        async with self.pool.acquire() as connect:
            select = await connect.execute(sql) 
            
    async def get_pair_of_key(self , text):
       sql = 'select name from pair_of_keys where name = $1'
       async with self.pool.acquire() as connect:
            select = await connect.fetchval(sql, text)
            return select
    
    async def add_pair_of_keys(self , name , text):
        sql = 'insert into pair_of_keys values($1, $2)'
        async with self.pool.acquire() as connect:
            select = await connect.execute(sql, *(name, text))
            
    async def add_key(self, name , key):
        sql = 'insert into keys values($1, $2)'
        async with self.pool.acquire() as connect:
            select = await connect.execute(sql, *(name, key))      
            
            
    async def get_all_pair_keys(self):
       sql = 'select name from pair_of_keys'
       async with self.pool.acquire() as connect:
            select = await connect.fetch(sql)
            lists = []
            for selec in select:
                lists.append(dict(selec))
            return lists 

    async def get_keys(self, name):
       sql = 'select key from keys where pair_of_keys = $1 '
       async with self.pool.acquire() as connect:
            select = await connect.fetch(sql, name)
            lists = []
            for selec in select:
                lists.append(dict(selec))
            return lists

    async def get_all_keys(self):
       sql = 'select * from keys'
       async with self.pool.acquire() as connect:
            select = await connect.fetch(sql)
            lists = []
            for s in select:
                lists.append(dict(s))
            return lists
        
            
    async def delete_key (self, name):
       sql = 'delete from keys where key = $1'
       async with self.pool.acquire() as connect:
           select = await connect.execute(sql, name) 
           
           
    async def update_text(self, name , text):
        sql = 'update pair_of_keys set message = $1 where name =$2'
        async with self.pool.acquire() as connect:
           select = await connect.execute(sql, *(text, name))
           
    async def get_text(self , pair_of_keys):
        sql = 'select message from pair_of_keys where name = $1'
        async with self.pool.acquire() as connect:
           select = await connect.fetchval(sql, pair_of_keys) 
           return select

    async def delete_piar_of_keys(self):
       sql = "delete from pair_of_keys"
       async with self.pool.acquire() as connect:
           select = await connect.execute(sql) 
           
    async def delete_keys(self):
       sql = "delete from keys"
       async with self.pool.acquire() as connect:
           select = await connect.execute(sql)    