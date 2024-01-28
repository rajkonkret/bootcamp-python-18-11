import sqlite3

data = [
    (5, 'Rust', 899),
    (6, 'Angular', 1899),
    (7, 'JS', 99),
]
try:
    sql_connection = sqlite3.connect('sqlite_python.db')  # baza w pliku
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    insert = '''
    INSERT INTO software (id,name,price) VALUES (?,?,?);
    '''

    # wpisanie do bazy elemntów gdzie dane zmienne
    # cursor.execute(insert, (4, 'Scala', 5600))
    # sql_connection.commit()

    # wrzucenie danych do bazy gdzie wiele rekordow umieszczone w jedej liscie
    cursor.executemany(insert, data)
    sql_connection.commit()


except sqlite3.Error as e:
    print("Błąd bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknieta")
