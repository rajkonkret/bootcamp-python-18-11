class PrintedMedia:
    def print_media(self):
        print("Drukowana treść")


class DigitalMedia:
    def digital_media(self):
        print("Cyfrowa treść")


class Book(PrintedMedia):
    pass


class Ebook(DigitalMedia):
    pass


class MultimediaBook(Book, Ebook):
    pass


mulimedia_ebook = MultimediaBook()
print(MultimediaBook.__mro__)
# (<class '__main__.MultimediaBook'>,
# <class '__main__.Book'>,
# <class '__main__.PrintedMedia'>,
# <class '__main__.Ebook'>,
# <class '__main__.DigitalMedia'>,
# <class 'object'>)
mulimedia_ebook.print_media()
mulimedia_ebook.digital_media()
# Drukowana treść
# Cyfrowa treść
