import tkinter as tk
import tkinter.font as tkFont


class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_879 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_879["font"] = ft
        GLabel_879["fg"] = "#333333"
        GLabel_879["justify"] = "center"
        GLabel_879["text"] = "label"
        GLabel_879.place(x=60, y=90, width=70, height=25)

        GButton_274 = tk.Button(root)
        GButton_274["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_274["font"] = ft
        GButton_274["fg"] = "#000000"
        GButton_274["justify"] = "center"
        GButton_274["text"] = "Button"
        GButton_274.place(x=250, y=40, width=70, height=25)
        GButton_274["command"] = self.GButton_274_command

        GCheckBox_727 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_727["font"] = ft
        GCheckBox_727["fg"] = "#333333"
        GCheckBox_727["justify"] = "center"
        GCheckBox_727["text"] = "CheckBox"
        GCheckBox_727.place(x=90, y=210, width=70, height=25)
        GCheckBox_727["offvalue"] = "0"
        GCheckBox_727["onvalue"] = "1"
        GCheckBox_727["command"] = self.GCheckBox_727_command

        GRadio_88 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_88["font"] = ft
        GRadio_88["fg"] = "#333333"
        GRadio_88["justify"] = "center"
        GRadio_88["text"] = "RadioButton"
        GRadio_88.place(x=300, y=210, width=85, height=25)
        GRadio_88["command"] = self.GRadio_88_command

        GLineEdit_695 = tk.Entry(root)
        GLineEdit_695["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_695["font"] = ft
        GLineEdit_695["fg"] = "#333333"
        GLineEdit_695["justify"] = "center"
        GLineEdit_695["text"] = "Entry"
        GLineEdit_695.place(x=60, y=40, width=70, height=25)

        GListBox_968 = tk.Listbox(root)
        GListBox_968["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_968["font"] = ft
        GListBox_968["fg"] = "#333333"
        GListBox_968["justify"] = "center"
        GListBox_968.place(x=200, y=310, width=80, height=25)

        GMessage_603 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_603["font"] = ft
        GMessage_603["fg"] = "#333333"
        GMessage_603["justify"] = "center"
        GMessage_603["text"] = "Message"
        GMessage_603.place(x=440, y=80, width=80, height=25)

        GLabel_863 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_863["font"] = ft
        GLabel_863["fg"] = "#333333"
        GLabel_863["justify"] = "center"
        GLabel_863["text"] = "label"
        GLabel_863.place(x=360, y=20, width=70, height=25)

    def GButton_274_command(self):
        print("command")

    def GCheckBox_727_command(self):
        print("command")

    def GRadio_88_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
