class Printer:
    def print_message(self, message):
        print(f"Drukowanie wiadomości {message}")


class Scanner:
    def scan_document(self):
        print("Skanowanie dokumentu")
        return "Zawartosc dokumentu"


class MulifunctionDevice(Printer, Scanner):
    def photocopy(self):
        content = self.scan_document()
        self.print_message(content)


device = MulifunctionDevice()
device.photocopy()
# Skanowanie dokumentu
# Drukowanie wiadomości Zawartosc dokumentu

message = device.scan_document()
# Skanowanie dokumentu

device.print_message(message)
# Drukowanie wiadomości Zawartosc dokumentu

print(MulifunctionDevice.__mro__)
# (<class '__main__.MulifunctionDevice'>, <class '__main__.Printer'>, <class '__main__.Scanner'>, <class 'object'>)
