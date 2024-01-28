import sqlite3

try:
    # sql_connection = sqlite3.connect('sqlite_python.db')  # baza w pliku
    # sql_connection = sqlite3.connect('test.db')  # baza w pliku
    sql_connection = sqlite3.connect('example.db')  # baza w pliku
    # sql_connection = sqlite3.connect(':memory:')  # baza danych w pamięci
    sql_connection.row_factory = sqlite3.Row  # chcemy aby zwracała jako słownik
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    table_data = 'users'
    # table_data = 'software'
    select = f'''SELECT * FROM {table_data};'''  # wczytaj (select) wszystko (*) z tabeli o nazwie {table_data}

    # wykonujemy select na bazie danych (pobranie danych) - baza w cursorze wystawia dane z tabeli np.: users
    cursor.execute(select)

    # """ Fetches all rows from the resultset. """ - Pobranie wszystkich elemntów za jednym razem
    # do zmiennej rows wrzucamy dane przygotowane przez baze danych za pomocą cursor
    rows = cursor.fetchall()  # pobieranie danych jakie wystawiła baza danych np.: po komendzie select
    # wyswietlamy dane zawrte w zmiennej rows w postaci słownika
    for row in rows:
        print(dict(row))

except sqlite3.Error as e:
    print("Błąd bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")
