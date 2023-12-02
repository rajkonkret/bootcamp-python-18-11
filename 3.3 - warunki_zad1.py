# warunki
# instrukcje sterowania przepływem programu
# if
# if warunek:
#   komenda do wykonanai gdy warunek spełniony

odp = True
if odp:
    print("Brawo")
else:
    print("ucz sie dalej")

print("Dalsze instrukcje w programie")

if True:
    pass  # nic nie rób

print("Dalej")

# kolejnośc warunków ma znaczenie
# po pierwszym True wychodzi z drzewka warunkó
# podatek = 0.9
# zarobki = float(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.9
# print(f"Płacisz {zarobki * podatek} podatku")
# # miedzy 10000 a 29999 podatek 0.2
# ctrl / - komentowanie wielu linijek

suma_zam = 50
if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabacik wynosi {rabacik}")

rabat = 25 if suma_zam > 150 else 0
print(f"Rabat wynosi {rabat}")

# zasymulujemy system zbierania logów
# w zaleznosci od tego jaki sytem i jaki bład przysle wykonamy rózne czynnsci
# console, email, inny
# critical, inny, medium


lista_bledow = []
alert_system = 'console'
error = 'critical'
error_message = 'Stało się coś strasznego'

# gdy przyjdzie z sytemu email wyswietlic komunikat error_message
if alert_system == "email":
    print(error_message)
elif alert_system == "console":
    print("System console")
    if error == 'medium':
        lista_bledow.append('ostrzeżenie')
    elif error == 'critical':
        lista_bledow.append("krytyczny")
else:
    print("Nie znam takiego systemu")
print(lista_bledow)

alert_dict = {'email': 'Coś poszło nie tak', 'console': {'critical': "krytyczny", 'medium': 'ostrzeżenie'}}
# if alert_system == 'email':
#     print(alert_dict[alert_system])
# elif alert_system == 'console':
print(alert_dict[alert_system])  # Coś poszło nie tak
if alert_system == 'email':
    print(alert_dict[alert_system])
elif alert_system == 'console':
    errors = alert_dict[alert_system]
    print(errors[error])

# zrobic program
# test z historii, z czegokolwiek

licznik = 0
odp = input("Podaj datę Chrztu Polski")
if odp == "966":
    print("Prawidłowa odpowiedź")
    licznik += 1
else:
    print("Błedna odpowiedź")
odp2 = input("Podaj stolicę Polski")
if odp2.lower() == 'warszawa':
    print("Prawidłowa odpowiedź")
    licznik += 1
print(f"Podałeś prawidłowych odpowiedzi: {licznik}")

odp = input("Podaj imie")
if odp.upper() in ["RADEK", "TOMEK", "KAROLINA", "MARTYNA", "PAULINA", "MATEUSZ", "WOJTEK"]:
    print("Odpowiedź prawidłowa")
else:
    print("Błąd")
# jupyter
# 13:35
