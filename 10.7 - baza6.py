import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')  # baza w pliku
    # sql_connection = sqlite3.connect(':memory:')  # baza danych w pamięci
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    # usunięcie elementów z bazy danych
    delete = '''
    DELETE FROM software WHERE id=1;
    '''
    update = '''
    UPDATE software SET price=2000 WHERE id=7;'''

    # komentujemy bo juz usunięte
    # cursor.execute(delete)
    # sql_connection.commit()

    cursor.execute(update)
    sql_connection.commit()

except sqlite3.Error as e:
    print("Błąd bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")
