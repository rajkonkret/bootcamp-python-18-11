# napisac program kalkulator z wykorzystaniem głownej petli while
# przechwycic możliwe wyjątki i obsłużyc
# ładnie wypisac wynik np.: Dodawanie 2 + 4 = 6
#
# wyswietlic opcje do wyboru (dodac opcje zakończenia)
# pobrac opcje od uzytkownika
# w zaleznosci od wybranej opcji wykonac działanie i wyswietlic wynik

while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)

    odp = input("Podaj działanie do wykonania")
    if odp == "5":
        break
    try:
        a = int(input("Podaj pierwszą lizbę"))
        b = int(input("Podaj drugą lizbę"))

        if odp == "1":
            print(f"Wynik dodawania {a} + {b} = {a + b}")
        elif odp == "2":
            print(f"Wynik odejmowania {a} - {b} = {a - b}")
        elif odp == "3":
            print(f"Wynik mnozenia {a} * {b} = {a * b}")
        elif odp == "4":
            print(f"Wynik dzielenia {a} / {b} = {a / b}")
        else:
            print("Nie znam takiego działania")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except ValueError:
        print("Błąd wartości")
    except  TypeError:
        print("Bład typu")
    except Exception as e:
        print("Błąd", e)
    else:
        print("Działąnie wykonane poprawnie")
    finally:
        print("Długo jeszcze?")
