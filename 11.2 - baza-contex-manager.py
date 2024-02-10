# context manager -> with
import sqlite3


class SQLiteDBContextManager:
    def __init__(self, db_name):  # metoda inicjalizująca - konstruktor
        self.db_name = db_name
        self.conn = None

    def __enter__(self):  # wykonuje sie przed zadaniem
        self.conn = sqlite3.connect(self.db_name)
        return self.conn  # zwracamy połaczenie z bazą

    def __exit__(self, exc_type, exc_val, exc_tb):  # wykonuje się zawsze
        if self.conn:
            self.conn.commit()
            self.conn.close()


lista = []
db_name = 'my_data.db'
# DBBrowser
# HiDi
# pgAdmin

with SQLiteDBContextManager(db_name) as conn:  # __enter__ zwróći nam połączenie
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT);')
    # cursor.execute('INSERT INTO users (name) VALUES (?);', ("John",))
    # cursor.execute('INSERT INTO users (name) VALUES (?);', ("Alice",))
    # cursor.execute('INSERT INTO users (name) VALUES (?);', ("Tom",))
    # cursor.execute('INSERT INTO users (name) VALUES (?);', ("Radek",))
    select = cursor.execute('SELECT * FROM users;')
    for i in select:
        print(i)
        lista.append(i)

print(lista)
# [(1, 'John'), (2, 'John'), (3, 'Alice'), (4, 'Tom'), (5, 'Radek'), (6, 'Radek'), (7, 'Radek')]
