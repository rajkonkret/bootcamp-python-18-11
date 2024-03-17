import sqlite3

sql_conn = None
try:
    sql_conn = sqlite3.connect('data/cantor.db')
    cursor = sql_conn.cursor()

    query = '''CREATE TABLE transactions(id INTEGER PRIMARY KEY AUTOINCREMENT,
    currency varchar(5),
    amount INT,
    user varchar(5),
    trans_date DATE NOT NULL DEFAULT(date()));
    '''

    create_users = '''CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password TEXT,
    is_active BOOLEAN NOT NULL DEFAULT 0,
    is_admin BOOLEAN NOT NULL DEFAULT 0
    );'''
    # cursor.execute(query)
    cursor.execute(create_users)

    sql_conn.commit()
except sqlite3.Error as e:
    print("Bład", e)
finally:
    if sql_conn:
        sql_conn.close()
