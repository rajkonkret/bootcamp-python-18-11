class Animal:

    def __init__(self, name):
        self.name = name

    def wydaj_odglos(self):
        pass

    def info(self):
        print(f"Imię: {self.name}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def wydaj_odglos(self):
        print("Hau Hau")

    def info(self):
        super().info()
        print(f"Rasa: {self.breed}")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def wydaj_odglos(self):
        print("Hau Hau")

    def info(self):
        super().info()
        print(f"Kolor: {self.color}")


class Tiger(Cat):

    def __init__(self, name, color, liczba_paskow):
        super().__init__(name, color)
        self.liczba_paskow = liczba_paskow

    def wydaj_odglos(self):
        print("ARR Arr!!!")

    def info(self):
        super().info()
        print(f"Liczba pasków: {self.liczba_paskow}")


animal1 = Animal('Bezimienny')
animal1.info()
animal1.wydaj_odglos()

dog1 = Dog("Burek", "Kundel")
dog1.info()
dog1.wydaj_odglos()

cat1 = Cat("Filemon", "Biały w ciapy")
cat1.info()
cat1.wydaj_odglos()

tiger = Tiger("Tygrysek", "Pomarańczowy", 15)
tiger.info()
tiger.wydaj_odglos()
