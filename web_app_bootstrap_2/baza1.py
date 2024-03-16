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

    cursor.execute(query)

    sql_conn.commit()
except sqlite3.Error as e:
    print("Bład", e)
finally:
    if sql_conn:
        sql_conn.close()
