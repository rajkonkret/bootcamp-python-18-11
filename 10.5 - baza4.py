import sqlite3

lista = []

try:
    sql_connection = sqlite3.connect('sqlite_python.db')  # baza w pliku
    sql_connection.row_factory = sqlite3.Row  # ustawiamy aby baza zwracała dane jako słownik
    cursor = sql_connection.cursor()

    # wyswietlanie zawartosci tabeli software
    select = '''
    SELECT * FROM software;
    '''
    # ctr / - komentowanie zznaczonego bloku kodu
    # for row in cursor.execute(select):
    #     print(row)
    #     lista.append(dict(row))
    #
    # print(lista)  # [{'id': 1, 'name': 'Python', 'price': 100.0}]

    # inne podejscie do select
    cursor.execute(select)
    # """ Fetches all rows from the resultset. """ - Pobranie wszystkich elemntów za jednym razem
    rows = cursor.fetchall()  # pobieranie danych jakie wystawiła baza danych np.: po komendzie select
    for row in rows:
        print(dict(row))  # {'id': 1, 'name': 'Python', 'price': 100.0}

    print("Baza danych została podłączona")
except sqlite3.Error as e:
    print("Błąd bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")
