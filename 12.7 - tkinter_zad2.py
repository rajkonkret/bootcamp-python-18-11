import tkinter as tk  # import jako alias


def on_click():
    print("Przycis został naciśnięty")


app = tk.Tk()  # tworzenie okienka
app.title("Przykład")

# definicja obiektu typu Button (guzik)
# na okienku app dodaje guzik
button = tk.Button(app, text="Kliknij mnie", command=on_click)
# command= podajemy adres metody do wykonania (nazwa bez nawiasów)
button.pack()

app.mainloop()  # wyswietlenie okienka
