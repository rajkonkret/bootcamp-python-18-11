import tkinter as tk


def on_value_changed(value):
    print(f"Zmieniona zawartość suwaka {value}")


app = tk.Tk()
app.title("Przykład suwaka")
# from_=0 - z podkreślnikiem na końcu
slider = tk.Scale(app, from_=0, to=100, orient=tk.HORIZONTAL, command=on_value_changed)
slider.pack(side=tk.BOTTOM)

app.mainloop()
