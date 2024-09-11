import tkinter as tk
from tkinter import messagebox
from login_modelo import LoginModel
from tkinter import PhotoImage
class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LoginApp")
        self.root.state("zoomed")

        self.frame = tk.Frame(root)
        self.frame.pack(expand=True)


        try:
            self.img = image.open("imagem/istockphoto.jpg")
            self.img = Image.Tk.PhotoImage(self.img)
            self.lblimg = tk.Label(self.frame, image=self.img)
            self.lblimg.grid(row=0, column=0, columnspan=2)  # Adiciona a imagem à grid
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")

        self.lblUsuario = tk.Label(self.frame, text="Usuário:", font=("Arial", 18))
        self.lblUsuario.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.txtUsuario = tk.Entry(self.frame, font=("Arial", 18))
        self.txtUsuario.grid(row=4, column=1, padx=10, pady=10)

        self.lblSenha = tk.Label(self.frame, text="Senha:", font=("Arial", 18))
        self.lblSenha.grid(row=5, column=0, padx=10, pady=10, sticky="e")
        self.txtSenha = tk.Entry(self.frame, font=("Arial", 18), show="*")
        self.txtSenha.grid(row=5, column=1, padx=10, pady=10)

        # Botão de Login
        self.btnLogin = tk.Button(self.frame, text="Login", font=("Arial", 18), command=self.realizar_login)
        self.btnLogin.grid(row=6, column=0, columnspan=2, pady=20)

        self.login_model = LoginModel()

    def realizar_login(self):
        usuario = self.txtUsuario.get()
        senha = self.txtSenha.get()

        usuario_encontrado = self.login_model.buscar_usuario(usuario)

        if usuario_encontrado:
            if usuario_encontrado[5] == senha:
                messagebox.showinfo("Login", "Login realizado com sucesso!")
                self.abrir_principal()
            else:
                messagebox.showerror("Login", "Senha incorreta.")
        else:
            messagebox.showerror("Login", "Usuário não encontrado.")

    def abrir_principal(self):
        self.root.destroy()
        subprocess.Popen(['python', 'principal.py'])

root = tk.Tk()
app = LoginApp(root)
root.mainloop()
