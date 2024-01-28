import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')  # baza w pliku
    # sql_connection = sqlite3.connect(':memory:')  # baza danych w pamięci
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    query = '''
    CREATE TABLE SqliteDB_developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL
    );'''

    # cursor.execute(query)  # wykonanie polecenia sql(query) na bazie danych
    # sql_connection.commit()  # utrwalenie zmian w bazie


except sqlite3.Error as e:
    print("Błąd bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")

# Baza danych została podłączona
# Baza została zamknieta
