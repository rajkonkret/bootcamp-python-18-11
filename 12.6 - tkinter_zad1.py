import tkinter


class MyGui:
    def __init__(self):
        self.main_window = tkinter.Tk()  # tworzenie okienka

        self.label = tkinter.Label(self.main_window, text="Witaj świecie")  # definicja labelki
        self.label2 = tkinter.Label(self.main_window, text="Radek")  # definicja labelki
        self.label3 = tkinter.Label(self.main_window, text="Python")  # definicja labelki
        self.label4 = tkinter.Label(self.main_window, text="Na dole")  # definicja labelki

        self.label.pack(side='left')  # umieszczenie labelki w odpowiednim miejscu ekranu
        self.label2.pack(side='right')  # umieszczenie labelki w odpowiednim miejscu ekranu
        self.label3.pack(side='top')  # umieszczenie labelki w odpowiednim miejscu ekranu
        self.label4.pack(side='bottom')  # umieszczenie labelki w odpowiednim miejscu ekranu

        tkinter.mainloop()  # uruchomienie okienka
        # right, top, bottom


my_gui = MyGui()
