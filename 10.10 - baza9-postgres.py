# Połączenie z zewnętrzną bazą sql typu postgress
import asyncio  # działąnia równoległe
import asyncpg


async def run():
    conn = await asyncpg.connect(user='', password='',
                                 database='', host='')
    await conn.fetch('''CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY, name TEXT);''')
    await conn.execute('''
    INSERT INTO users (name) VALUES ($1);
    ''', 'John')
    await conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
# https://www.pgadmin.org
