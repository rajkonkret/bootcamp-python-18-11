tekst = "Witaj świecie"
print(tekst)
print(type(tekst))  # <class 'str'>
# zwraca kopie ze zmianami. Musimy ją sobie zapamiętac. Np.: w nowej zmiennej tekst2
tekst2 = tekst.upper()  # """ Return a copy of the string converted to uppercase. """
print(tekst2)  # WITAJ ŚWIECIE
print(tekst)  # Witaj świecie
# sprawdzic co robi lower, capitalize
print(tekst.lower())  # witaj świecie
print(tekst.capitalize())  # Witaj świecie
print(tekst.title())  # Witaj Świecie
# stringi są niemutowalne
# Radek - ciag znaków
name = "Radek"
#       01234
print(len(name))  # len() - sprawdzenie długosci tekstu czyli 5
# indeksowanie tekstu zaczyna sie od zera
print(name[0])  # pierwsza literka tekstu
print(name[1])
print(name[2])
print(name[3])
print(name[4])  # ostatnia litera tego tekstu indeks 4, bo numerowane od 0
print(name[2:4])  # de od indeksu 2 do 3 bo 4 nie wchodzi w zakres. zbior z prawej strony otwarty
print(name[:4])  # Rade 0..3
str1 = "HELLO PYTHON"
# stringi są niemutowalne
# str1[0:5] = "HOLAA"  # TypeError: 'str' object does not support item assignment
print(str1)  # HELLO PYTHON
my_str = "   Hello Everyone   "
print(my_str)  # "   Hello Everyone   "
print(my_str.strip())  # Hello Everyone - usunięcie bialych znaków (np.: spacji) z początku i końća tekstu
print(my_str.rstrip())  # "   Hello Everyone" - usuniecie białych znaków z prawej strony
print(my_str.lstrip())  # "Hello Everyone   " - usunięcie z lewej strony

my_str2 = '****Hello****World****'
print(my_str2.strip("*"))  # "Hello****World" - mozna wskazac by usuwał początkowe i końćowe konkretne znaki
print(my_str2.rstrip("*"))  # "****Hello****World"
print(my_str2.lstrip("*"))  # "Hello****World****"
print(my_str2)
print(my_str)
print(tekst)
# ****Hello****World****
#    Hello Everyone
# Witaj świecie
print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst.removesuffix("świecie"))  # "Witaj "

print(tekst.count("i"))  # 3 policzenie wystąpien danego znaku(wyrazu)
print(tekst.count("i", 0, 4))  # 1, od 0..3 4 - nie brana pod uwage
print(tekst.count("j", 0, 4))  # 0, od 0..3 4 - nie brana pod uwage

print(my_str2)  # ****Hello****World****
print(my_str2.replace("He", 'Ho'))  # ****Hollo****World****, zamiana He na Ho
print(my_str)  # "   Hello Everyone   "
print(my_str.replace(" ", ""))  # HelloEveryone - zamiana wszystkich " " na pusty znak ""
print(my_str.center(80))  # wycentrowanie do długosci 80
# "                                 Hello Everyone                                 "
print(tekst.index("św"))  # 6, odszukanie indeksu dla znków "św"
print("Mój ulubiony serial \"Alternatywy 4\"")  # Mój ulubiony serial "Alternatywy 4"
# \ - w stringu tzw znak ucieczki, oznacza, nie interpretuj kolejnego znaku tylko po prostu wyswietl

imie = "Radek"
# f-stringi - sformatowany tekst
formated_text = f"Mam na imię {imie} i lubię Pythona"
print(formated_text)  # Mam na imię Radek i lubię Pythona
formated_text2 = f"\tMam na imię {imie}\n i lubię Pythona\b"
print(formated_text2)
# "	Mam na imię Radek
#  i lubię Python"
# \t - tabulator
# \n - nowa linia
# \b - backspace
starszy = "Witaj %s!"
print(starszy % imie)  # Witaj Radek!
print("Witaj {}!".format(imie))  # tekst sformatowany za pomoca format - zamiast literki "f"
# Witaj Radek!

print("""
Tekst
    wielolinijkowy""")
# Tekst
#     wielolinijkowy

# kodowanie znaków, np.: utf-8, windows-1250
encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie' zapisany w postaci bajtowej tekst wraz ze znakami sterującymi
# b - tekst bajtowy ( binarny)
# \xc5 - liczbe zapisana w systemie 16 - c5 = 197, 9b = 155
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie
# 15:12

