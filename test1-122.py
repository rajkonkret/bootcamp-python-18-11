# unittesty - testy jednostkowe
# pytetst - funkcja do testowania
# Asercja w Pythonie to instrukcja służąca do sprawdzania poprawności założeń w kodzie.
# Jeśli wyrażenie w asercji jest prawdziwe (True), program kontynuuje działanie.
# Jeśli jest fałszywe (False), Python zgłasza wyjątek AssertionError,
# co często służy do wychwycenia błędów w kodzie podczas fazy rozwoju i testowania.
# pip install pytest
# pytest test1-122.py  - uruchomienie testów w pliku
# cd katalog - wejscie do katalogu
# strzałka w góre - wywołanie ostatniej komendy z historii
from unittest import TestCase


class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)  # asercje

    def test_uppercase(self):
        assert 'python'.upper() == 'PYTHON'  # sprawdź

    def test_reversed(self):
        assert list(reversed([1, 2, 3])) == [3, 2, 1]

    def test_always_fall(self):
        self.assertTrue(False)