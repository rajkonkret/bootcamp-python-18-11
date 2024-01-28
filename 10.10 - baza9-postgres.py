# Połączenie z zewnętrzną bazą sql typu postgress
import asyncio  # działąnia równoległe
import asyncpg


async def run():
    conn = await asyncpg.connect(user='37970432_dane', password='Radito_02',
                                 database='37970432_dane', host='serwer2348480.home.pl')
    await conn.fetch('''CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY, name TEXT);''')
    await conn.execute('''
    INSERT INTO users (name) VALUES ($1);
    ''', 'John')
    await conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
# https://www.pgadmin.org