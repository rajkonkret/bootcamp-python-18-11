from pprint import pprint


class ContactList(list['Contact']):  # ['Contact'] tylko podpowiedź
    def search(self, name):
        matching_contacts = []
        for c in self:
            if name in c.name:
                matching_contacts.append(c)
        return matching_contacts


class Contact:
    all_contacts = ContactList()  # [] Tworzenie pustej listy z klasy ContactList

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        # {self.__class__.__name__} wypisanie nazwy klasy obiektu
        return f"{self.__class__.__name__} {self.name!r} {self.email!r}"


class Suplier(Contact):
    """
    Klasa Suplier dziedziczy po klasie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")

    def __repr__(self):
        # {self.__class__.__name__} wypisanie nazwy klasy obiektu
        return f"{self.__class__.__name__} {self.name} {self.email}"


class Friend(Suplier):
    """
    Klasa dziedziczy po Suplier
    """

    def __init__(self, name, mail, phone='000000'):
        super().__init__(name, mail)
        self.phone = phone

    def __repr__(self):
        # {self.__class__.__name__} wypisanie nazwy klasy obiektu
        return f"{self.__class__.__name__} {self.name} {self.email} +48 {self.phone}"


# lista = []
# lista.search() - nie posiada

# search?
c_l = ContactList()  # dziedzicza metody z listy,
# de facto jest to lista o rozszerzonym działaniu (serach)
print(c_l)
print(type(c_l))  # <class '__main__.ContactList'>
c1 = Contact("Adam", "adam@wp.pl")
c2 = Contact("Radek", "radek@wp.pl")
c3 = Contact("Tomek", "Tomek@wp.pl")
c_l.append(c1)
c_l.append(c2)
c_l.append(c3)
print(c_l)  # [Contact Adam adam@wp.pl, Contact Radek radek@wp.pl, Contact Tomek Tomek@wp.pl]
print(c_l.search('Adam'))  # [Contact Adam adam@wp.pl]
print(c1.all_contacts)  # [Contact Adam adam@wp.pl, Contact Radek radek@wp.pl, Contact Tomek Tomek@wp.pl]
print(c1.all_contacts.search("Adam"))  # [Contact Adam adam@wp.pl]
# kolejnosc rozwiazywania nazw obiektów
print(ContactList.__mro__)  # (<class '__main__.ContactList'>, <class 'list'>, <class 'object'>)
print(Contact)  # <class '__main__.Contact'>
print(Contact.__name__)  # Contact
# !r dodaje cudzusłowia do stringów itp
# [Contact 'Adam' 'adam@wp.pl', Contact 'Radek' 'radek@wp.pl', Contact 'Tomek' 'Tomek@wp.pl']
pprint(c1.all_contacts)  # ładne wyswietlenie
# [Contact 'Adam' 'adam@wp.pl',
#  Contact 'Radek' 'radek@wp.pl',
#  Contact 'Tomek' 'Tomek@wp.pl']
l_test = [c1]
pprint(l_test)  # [Contact 'Adam' 'adam@wp.pl']

s1 = Suplier("Jarek", "jarek@wp.pl")
print(s1)  # Suplier Jarek jarek@wp.pl
pprint(s1)  # Suplier Jarek jarek@wp.pl
pprint(s1.all_contacts)
# [Contact 'Adam' 'adam@wp.pl',
#  Contact 'Radek' 'radek@wp.pl',
#  Contact 'Tomek' 'Tomek@wp.pl',
#  Suplier Jarek jarek@wp.pl]
print(Suplier.__mro__)  # (<class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)
print(Friend.__mro__)
# (<class '__main__.Friend'>, <class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)
f1 = Friend("Marin", "marcin@onet.pl")
print(f1)  # Friend Marin marcin@onet.pl, po dodaniu phone Friend Marin marcin@onet.pl +48 000000
print(f1.all_contacts)
f1.order("Kawa")  # Kawa zamówiono od Marin
f2 = Friend("Ania", "ania@wp.pl", '123456789')
print(f2)  # Friend Ania ania@wp.pl +48 123456789
pprint(f2.all_contacts)
# [Contact 'Adam' 'adam@wp.pl',
#  Contact 'Radek' 'radek@wp.pl',
#  Contact 'Tomek' 'Tomek@wp.pl',
#  Suplier Jarek jarek@wp.pl,
#  Friend Marin marcin@onet.pl +48 000000,
#  Friend Ania ania@wp.pl +48 123456789]

print(f2.all_contacts.search('Jarek'))
# [Suplier Jarek jarek@wp.pl]