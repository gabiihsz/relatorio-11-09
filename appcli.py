import tkinter as tk
from tkinter import messagebox, ttk
import os
from clientes import Cliente
from cidade import Cidade

class Application:
    def _init_(self, root):
        self.cliente = Cliente()
        self.cidade = Cidade(root)
        self.root = root
        self.root.title("Cadastro de Clientes")

        # Widgets
        self.lblIdCliente = tk.Label(root, text="ID do Cliente:")
        self.lblIdCliente.grid(row=0, column=0)
        self.txtIdCliente = tk.Entry(root)
        self.txtIdCliente.grid(row=0, column=1)

        self.btnBuscar = tk.Button(root, text="Buscar", command=self.buscar_cliente)
        self.btnBuscar.grid(row=0, column=2)

        self.lblNome = tk.Label(root, text="Nome:")
        self.lblNome.grid(row=1, column=0)
        self.txtNome = tk.Entry(root)
        self.txtNome.grid(row=1, column=1)

        self.lblTelefone = tk.Label(root, text="Telefone:")
        self.lblTelefone.grid(row=2, column=0)
        self.txtTelefone = tk.Entry(root)
        self.txtTelefone.grid(row=2, column=1)

        self.lblEmail = tk.Label(root, text="E-mail:")
        self.lblEmail.grid(row=3, column=0)
        self.txtEmail = tk.Entry(root)
        self.txtEmail.grid(row=3, column=1)

        self.lblcidade = tk.Label(root, text="Cidade:")
        self.lblcidade.grid(row=4, column=0)

        # Dropdown para cidades
        self.varcidade = tk.StringVar(root)
        self.cidade_disponiveis = self.listar_cidades()
        if self.cidade_disponiveis:
            self.varcidade.set(self.cidade_disponiveis[0])  # Define a primeira cidade como padrão
        else:
            self.varcidade.set("Nenhuma cidade cadastrada")  # Caso não haja cidades, deixa o dropdown vazio

        self.dropdowncidade = tk.OptionMenu(root, self.varcidade, *self.cidade_disponiveis)
        self.dropdowncidade.grid(row=4, column=1)

        # Botões
        self.btnInserir = tk.Button(root, text="Inserir", command=self.inserir_cliente)
        self.btnInserir.grid(row=5, column=0)

        self.btnAlterar = tk.Button(root, text="Alterar", command=self.alterar_cliente)
        self.btnAlterar.grid(row=5, column=1)

        self.btnExcluir = tk.Button(root, text="Excluir", command=self.excluir_cliente)
        self.btnExcluir.grid(row=5, column=2)

        self.lblMensagem = tk.Label(root, text="")
        self.lblMensagem.grid(row=6, column=0, columnspan=3)

        # Treeview para listar os clientes
        self.tree = ttk.Treeview(root, columns=("id", "nome", "telefone", "email", "cidade"), show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("nome", text="Nome")
        self.tree.heading("telefone", text="Telefone")
        self.tree.heading("email", text="E-mail")
        self.tree.heading("cidade", text="Cidade")

        self.tree.column("id", width=50)
        self.tree.column("nome", width=150)
        self.tree.column("telefone", width=100)
        self.tree.column("email", width=200)
        self.tree.column("cidade", width=100)

        self.tree.grid(row=7, column=0, columnspan=4, sticky="nsew")

        # Correção na criação da barra de rolagem para o Treeview
        self.scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=7, column=4, sticky='ns')

        # Carrega os clientes no Treeview
        self.carregar_clientes()

        # Bind para detectar o fechamento da janela
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def listar_cidades(self):
        try:
            cursor = self.cliente.banco.conexao.cursor()  # Utiliza a conexão do banco de dados do cliente
            cursor.execute("SELECT nome FROM cidade")  # Ajuste a query conforme o nome real da tabela e coluna
            cidades = [row[0] for row in cursor.fetchall()]  # Constrói a lista com os nomes das cidades
            return cidades if cidades else ["Nenhuma cidade cadastrada"]
        except Exception as e:
            print(f"Erro ao carregar cidades: {e}")  # Exibe o erro no console para depuração
        return ["Erro ao carregar cidades"]

    def buscar_cliente(self):
        idCliente = self.txtIdCliente.get()
        if not idCliente:
            self.atualizar_mensagem("ID do cliente não pode estar vazio!", "error")
            return

        resultado = self.cliente.buscar(idCliente)
        if resultado:
            self.txtNome.delete(0, tk.END)
            self.txtNome.insert(tk.END, resultado[1])
            self.txtTelefone.delete(0, tk.END)
            self.txtTelefone.insert(tk.END, resultado[2])
            self.txtEmail.delete(0, tk.END)
            self.txtEmail.insert(tk.END, resultado[3])
            cidade_id = resultado[4]
            cidade_nome = self.obter_nome_cidade_por_id(cidade_id)
            if cidade_nome in self.cidade_disponiveis:
                self.varcidade.set(cidade_nome)
            self.atualizar_mensagem("Busca realizada com sucesso!")
        else:
            self.atualizar_mensagem("Cliente não encontrado!", "error")

    def obter_nome_cidade_por_id(self, cidade_id):
        try:
            cursor = self.cliente.banco.conexao.cursor()
            cursor.execute("SELECT nome FROM cidade WHERE idcid=?", (cidade_id,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else "Cidade não encontrada"
        except Exception as e:
            print(f"Erro ao buscar nome da cidade: {e}")
            return "Erro ao buscar cidade"

    def inserir_cliente(self):
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        cidade_nome = self.varcidade.get()

        if not nome or not telefone or not email or not cidade_nome:
            self.atualizar_mensagem("Todos os campos devem ser preenchidos!", "error")
            return

        cidade_id = self.obter_id_cidade_por_nome(cidade_nome)
        if cidade_id == "Erro ao buscar cidade":
            self.atualizar_mensagem("Erro ao buscar cidade!", "error")
            return

        self.cliente.inserir(nome, telefone, email, cidade_id)
        self.atualizar_mensagem("Cliente inserido com sucesso!")
        self.carregar_clientes()

    def obter_id_cidade_por_nome(self, cidade_nome):
        try:
            cursor = self.cliente.banco.conexao.cursor()
            cursor.execute("SELECT idcid FROM cidade WHERE nome=?", (cidade_nome,))
            resultado = cursor.fetchone()
            return resultado[0] if resultado else "Erro ao buscar cidade"
        except Exception as e:
            print(f"Erro ao buscar ID da cidade: {e}")
            return "Erro ao buscar cidade"

    def alterar_cliente(self):
        idCliente = self.txtIdCliente.get()
        nome = self.txtNome.get()
        telefone = self.txtTelefone.get()
        email = self.txtEmail.get()
        cidade_nome = self.varcidade.get()

        if not idCliente:
            self.atualizar_mensagem("ID do cliente não pode estar vazio!", "error")
            return

        cidade_id = self.obter_id_cidade_por_nome(cidade_nome)
        if cidade_id == "Erro ao buscar cidade":
            self.atualizar_mensagem("Erro ao buscar cidade!", "error")
            return

        self.cliente.alterar(idCliente, nome, telefone, email, cidade_id)
        self.atualizar_mensagem("Cliente alterado com sucesso!")
        self.carregar_clientes()

    def excluir_cliente(self):
        idCliente = self.txtIdCliente.get()
        if not idCliente:
            self.atualizar_mensagem("ID do cliente não pode estar vazio!", "error")
            return

        self.cliente.excluir(idCliente)
        self.atualizar_mensagem("Cliente excluído com sucesso!")
        self.carregar_clientes()

    def carregar_clientes(self):
        """Função para carregar os dados dos clientes no Treeview"""
        # Limpa os dados antigos
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Carrega os novos dados
        for cliente in self.cliente.listar_todos():

            self.tree.insert("", "end", values=(cliente[0], cliente[1], cliente[2], cliente[3], cliente[4]))

    def atualizar_mensagem(self, mensagem, tipo="info"):
        """Atualiza a mensagem na interface com cores diferentes dependendo do tipo."""
        if tipo == "info":
            self.lblMensagem.config(text=mensagem, fg="green")
        else:
            self.lblMensagem.config(text=mensagem, fg="red")

    def on_closing(self):
        self.root.destroy()
        os.system('python principal.py')

if __name__ == "_main_":
    root = tk
    Application(root)
    root.state("zoomed")
    root.mainloop()
