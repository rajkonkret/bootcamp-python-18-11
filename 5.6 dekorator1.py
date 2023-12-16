# dekorator - funkcja opakowująca inną w funkcję w dodatkową funkcjonalność
# @nazwa_dekoratora

def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()  # zwracamy wynik wykonania funkcji

    return wew  # zwracamy referencje (adres) funkcji


@dekor  # użycie dekoratora
def hej():
    print("Hej!!")


hej()  # Hej!!
# po uzyciu dekoratora @dekor - wynik jest taki:
# Dekorujemy
# Hej!!
