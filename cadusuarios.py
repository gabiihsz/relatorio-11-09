import tkinter as tk
from tkinter import *
from usuarios import Usuarios

class Usuario:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Gerenciamento de Usuários")
        self.master.geometry("800x600")


        self.fontepadrao = ("Arial", 14)
        self.fontebotao = ("Calibri", 13)

        # Main Frame
        self.janela = Frame(master)
        self.janela.pack(padx=20, pady=10)

        # TITULO
        self.titulo = Label(self.janela, text="Informe os Dados:", font=("Calibri", "30", "italic", "bold"))
        self.titulo.pack()
        self.titulo2 = Label(self.janela, text="Usuários\n", font=("Calibri", "20", "italic"))
        self.titulo2.pack()

        # ID USUARIO
        self.janela2 = Frame(master)
        self.janela2.pack(padx=20, pady=5)
        self.idLabel = Label(self.janela2, text="idUsuário:", font=self.fontepadrao)
        self.idLabel.pack(side=LEFT)
        self.id = Entry(self.janela2, width=18, font=self.fontepadrao)
        self.id.pack(side=LEFT)
        self.buscar = Button(self.janela2, text="Buscar", font=self.fontebotao, width=10, command=self.buscarUsuario)
        self.buscar.pack(side=LEFT)

        # Nome
        self.janela3 = Frame(master)
        self.janela3.pack(padx=20, pady=5)
        self.nomeLabel = Label(self.janela3, text="Nome:", font=self.fontepadrao)
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.janela3, width=30, font=self.fontepadrao)
        self.nome.pack(side=LEFT)

        # Telefone
        self.janela4 = Frame(master)
        self.janela4.pack(padx=20, pady=5)
        self.telLabel = Label(self.janela4, text="Telefone:", font=self.fontepadrao)
        self.telLabel.pack(side=LEFT)
        self.tel = Entry(self.janela4, width=30, font=self.fontepadrao)
        self.tel.pack(side=LEFT)

        # Email
        self.janela5 = Frame(master)
        self.janela5.pack(padx=20, pady=5)
        self.emailLabel = Label(self.janela5, text="E-mail:", font=self.fontepadrao)
        self.emailLabel.pack(side=LEFT)
        self.email = Entry(self.janela5, width=30, font=self.fontepadrao)
        self.email.pack(side=LEFT)

        # Usuário
        self.janela6 = Frame(master)
        self.janela6.pack(padx=20, pady=5)
        self.usuLabel = Label(self.janela6, text="Usuário:", font=self.fontepadrao)
        self.usuLabel.pack(side=LEFT)
        self.usu = Entry(self.janela6, width=30, font=self.fontepadrao)
        self.usu.pack(side=LEFT)

        # Senha
        self.janela7 = Frame(master)
        self.janela7.pack(padx=20, pady=5)
        self.senhaLabel = Label(self.janela7, text="Senha:", font=self.fontepadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.janela7, width=30, font=self.fontepadrao, show="*")
        self.senha.pack(side=LEFT)

        # Buttons
        self.janela8 = Frame(master)
        self.janela8.pack(padx=20, pady=10)
        self.inserir = Button(self.janela8, text="Inserir", font=self.fontebotao, width=10, command=self.inserirUsuario)
        self.inserir.pack(side=LEFT)
        self.alt = Button(self.janela8, text="Alterar", font=self.fontebotao, width=10, command=self.alterarUsuario)
        self.alt.pack(side=LEFT)
        self.excluir = Button(self.janela8, text="Excluir", font=self.fontebotao, width=10, command=self.excluirUsuario)
        self.excluir.pack(side=LEFT)
        self.voltar = Button(self.janela8, text="Voltar", font=self.fontebotao, width=10, command=self.abrir_principal)
        self.voltar.pack(side=LEFT)

    def abrir_principal(self):
        import principal
        principal.main()

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.id.get()
        result = user.selectUser(idusuario)
        self.idLabel["text"] = result
        if user.idusuario:
            self.id.delete(0, END)
            self.id.insert(INSERT, user.idusuario)
            self.nome.delete(0, END)
            self.nome.insert(INSERT, user.nome)
            self.tel.delete(0, END)
            self.tel.insert(INSERT, user.telefone)
            self.email.delete(0, END)
            self.email.insert(INSERT, user.email)
            self.usu.delete(0, END)
            self.usu.insert(INSERT, user.usuario)
            self.senha.delete(0, END)
            self.senha.insert(INSERT, user.senha)

    def inserirUsuario(self):
        user = Usuarios()
        user.nome = self.nome.get()
        user.telefone = self.tel.get()
        user.email = self.email.get()
        user.usuario = self.usu.get()
        user.senha = self.senha.get()
        self.idLabel["text"] = user.insertUser()
        self.clearFields()

    def alterarUsuario(self):
        user = Usuarios()
        user.idusuario = self.id.get()
        user.nome = self.nome.get()
        user.telefone = self.tel.get()
        user.email = self.email.get()
        user.usuario = self.usu.get()
        user.senha = self.senha.get()
        self.idLabel["text"] = user.updateUser()
        self.clearFields()

    def excluirUsuario(self):
        user = Usuarios()
        user.idusuario = self.id.get()
        self.idLabel["text"] = user.deleteUser()
        self.clearFields()

    def clearFields(self):
        self.id.delete(0, END)
        self.nome.delete(0, END)
        self.tel.delete(0, END)
        self.email.delete(0, END)
        self.usu.delete(0, END)
        self.senha.delete(0, END)


if __name__ == "__main__":
    root = Tk()
    app = Usuario(root)
    root.mainloop()
