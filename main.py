import tkinter
from tkinter import *
class principal:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()

        self.msg = Label(self.widget1, text="Agenda")
        self.msg["font"] = ("Verdana", "20", "italic", "bold")
        self.msg.pack()

        self.usuarios = Button(self.widget1)
        self.usuarios.pack()
        self.usuarios["text"] = "Usuarios"
        self.usuarios["font"] = ("calibri", "20")
        self.usuarios["width"] = 10
        self.usuarios.pack()

        self.cidades = Button(self.widget1)
        self.cidades.pack()
        self.cidades["text"] = "Cidades"
        self.cidades["font"] = ("calibri", "20")
        self.cidades["width"] = 10
        self.cidades.pack()

        self.clientes = Button(self.widget1)
        self.clientes.pack()
        self.clientes["text"] = "Clientes"
        self.clientes["font"] = ("calibri", "20")
        self.clientes["width"] = 10
        self.clientes.pack()

        self.fechar = Button(self.widget1)
        self.fechar.pack()
        self.fechar["text"] = "Fechar"
        self.fechar["font"] = ("calibri", "20")
        self.fechar["width"] = 10
        self.fechar["command"] = self.widget1.quit
        self.fechar.pack()


root = Tk()
principal(root)
root.mainloop()
root.state("zoomed")

