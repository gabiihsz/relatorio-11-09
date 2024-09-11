from tkinter import *
from cidade import Cidade


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Cidades")

        self.lblidcidade = Label(root, text="Código")
        self.lblidcidade.grid(row=0, column=0, padx=10, pady=5)
        self.txtidcidade = Entry(root)
        self.txtidcidade.grid(row=0, column=1, padx=10, pady=5)

        self.lblnomecidade = Label(root, text="Nome da Cidade")
        self.lblnomecidade.grid(row=1, column=0, padx=10, pady=5)
        self.txtnomecidade = Entry(root)
        self.txtnomecidade.grid(row=1, column=1, padx=10, pady=5)

        self.lbluf = Label(root, text="UF")
        self.lbluf.grid(row=2, column=0, padx=10, pady=5)
        self.txtuf = Entry(root)
        self.txtuf.grid(row=2, column=1, padx=10, pady=5)

        self.lblmsg = Label(root, text="", fg="red")
        self.lblmsg.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.btnBuscar = Button(root, text="Buscar", command=self.buscarCidade)
        self.btnBuscar.grid(row=4, column=0, padx=10, pady=5)

        self.btnInsert = Button(root, text="Inserir", command=self.inserirCidade)
        self.btnInsert.grid(row=4, column=1, padx=10, pady=5)

        self.btnAlterar = Button(root, text="Alterar", command=self.alterarCidade)
        self.btnAlterar.grid(row=5, column=0, padx=10, pady=5)

        self.btnExcluir = Button(root, text="Excluir", command=self.excluirCidade)
        self.btnExcluir.grid(row=5, column=1, padx=10, pady=5)

    def buscarCidade(self):
        cidade = Cidade()
        idcidade = self.txtidcidade.get()
        cidade.selectCidade(idcidade)

        if cidade.idcidade:
            self.lblmsg["text"] = "Cidade encontrada!"
            self.txtidcidade.delete(0, END)
            self.txtidcidade.insert(INSERT, cidade.idcidade)
            self.txtnomecidade.delete(0, END)
            self.txtnomecidade.insert(INSERT, cidade.nomecidade)
            self.txtuf.delete(0, END)
            self.txtuf.insert(INSERT, cidade.uf)
        else:
            self.lblmsg["text"] = "Cidade não encontrada."

    def inserirCidade(self):
        cidade = Cidade()
        cidade.idcidade = self.txtidcidade.get()
        cidade.nomecidade = self.txtnomecidade.get()
        cidade.uf = self.txtuf.get()
        resultado = cidade.insertCidade()
        self.lblmsg["text"] = resultado
        self.limparCampos()

    def alterarCidade(self):
        cidade = Cidade()
        cidade.idcidade = self.txtidcidade.get()
        cidade.nomecidade = self.txtnomecidade.get()
        cidade.uf = self.txtuf.get()
        resultado = cidade.updateCidade()
        self.lblmsg["text"] = resultado
        self.limparCampos()

    def excluirCidade(self):
        cidade = Cidade()
        cidade.idcidade = self.txtidcidade.get()
        resultado = cidade.deleteCidade()  # Corrigi para usar o método correto
        self.lblmsg["text"] = resultado
        self.limparCampos()

    def limparCampos(self):
        self.txtidcidade.delete(0, END)
        self.txtnomecidade.delete(0, END)
        self.txtuf.delete(0, END)

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
