from pprint import pprint


class LongestKeyDict(dict):
    def longest_key(self):
        """
        :return: najdłuższy klucz ze słownika
        """
        longest = None
        for key in self:  # zwraca klucze
            if longest is None or len(key) > len(longest):
                longest = key

        return longest


# print(len(None))  # TypeError: object of type 'NoneType' has no len()

art = LongestKeyDict()
art['tomasz'] = 12
art['abraham'] = 7
art['zen'] = 1
print(art.longest_key())  # abraham
# assert słuzy do sprawdzenia poprawnosci wyniku
# assert warunek, komunikat błedu
assert 'abraham' == art.longest_key(), "Znalazł prawidłowo"  # nie ma błedu nie rzucił wyjątkiem
# assert 'zen' == art.longest_key(), "Znalazł błednie"  # AssertionError: Znalazł błednie
pprint(art)  # {'abraham': 7, 'tomasz': 12, 'zen': 1}
