import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')  # baza w pliku
    # sql_connection = sqlite3.connect(':memory:')  # baza danych w pamięci
    cursor = sql_connection.cursor()

    # w bazch danych pojedynczy cudzysłów ' tzw: ciapki
    # dodawnie rekordu do bazy
    insert = '''
    INSERT INTO software (id,name,price) VALUES(1,'Python',100);
    '''

    # wyswietlanie zawartosci tabeli software
    select = '''
    SELECT * FROM software;
    '''

    # wykonanie jednego polecenia na bazie
    # komentujemy by nie dodawac takiego samego rekordu
    # cursor.execute(insert)
    # sql_connection.commit()

    for row in cursor.execute(select):
        print(row)  # (1, 'Python', 100.0)

    print("Baza danych została podłączona")
except sqlite3.Error as e:
    print("Błąd bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")
