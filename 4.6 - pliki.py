# praca z plikami
# t = open("nazwapliku", "parametr")
# context manager
# klasa, któa ułatwia pracę np.: z plikami
# pomaga dbać o bezpieczeństwo procesu
# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     'U'       universal newline mode (deprecated)
#     ========= ===============================================================

# with open("test.log") takie samo ustawienie parametrów
# with open("test.log", "rt)
with open("test.log", "wt", encoding='utf-8') as fh:  # filehandler,'w' open for writing, truncating the file first
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze jedno\n")

# w - kasuje plik jesli istnieje, tworzy nowy plik
with open('test.log', 'w', encoding='utf-8') as file:
    file.write("Radek\n")
# # x - gdy plik istnieje dostaniemy błąd.
# with open('test.log', "x") as f:  # FileExistsError: [Errno 17] File exists: 'test.log'
#     f.write("Radek\n")

# with open('test2.log', "x") as f:
#     f.write("Radek\n")

with open("test.log", "a", encoding='utf-8') as file:
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dośdane\n")
    file.write("Dośąćńdane\n")

with open("test.log", "r", encoding='utf-8') as f:
    lines = f.read()

print(lines)  # Dośdane
