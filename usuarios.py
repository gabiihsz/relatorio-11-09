from Banco import Banco

class Usuarios:
    def __init__(self, idusuario=0, nome="", telefone="", email="", usuario="", senha=""):
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha
        self.banco = Banco()
    def insertUser(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("INSERT INTO tbl_usuarios (nome, telefone, email, usuario, senha) VALUES (?, ?, ?, ?, ?)",
                      (self.nome, self.telefone, self.email, self.usuario, self.senha))
            self.banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except Exception as e:
            print(f"Erro: {e}")
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("UPDATE tbl_usuarios SET nome = ?, telefone = ?, email = ?, usuario = ?, senha = ? WHERE idusuario = ?",
                      (self.nome, self.telefone, self.email, self.usuario, self.senha, self.idusuario))
            self.banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except Exception as e:
            print(f"Erro: {e}")
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):
        try:
            c = self.banco.conexao.cursor()
            c.execute("DELETE FROM tbl_usuarios WHERE idusuario = ?", (self.idusuario,))
            self.banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except Exception as e:
            print(f"Erro: {e}")
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idusuario):
        try:
            c = self.banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_usuarios WHERE idusuario = ?", (idusuario,))
            row = c.fetchone()
            if row:
                self.idusuario, self.nome, self.telefone, self.email, self.usuario, self.senha = row
                c.close()
                return "Busca feita com sucesso!"
            else:
                c.close()
                return "Usuário não encontrado!"
        except Exception as e:
            print(f"Erro: {e}")
            return "Ocorreu um erro na busca do usuário"
