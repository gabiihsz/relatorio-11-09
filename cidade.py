from Banco import Banco

class Cidade:
    def _init_(self, Cod_cidade=0, nome_cidade="", Uf=""):
        self.Cod_cidade = Cod_cidade
        self.nome_cidade = nome_cidade
        self.Uf = Uf

    def insertcid(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            INSERT INTO tbl_cidade (nome_cidade, Uf)
            VALUES (?, ?)
            """, (self.nome_cidade, self.Uf))
            banco.conexao.commit()
            c.close()
            return "Cidade cadastrada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção da cidade: {str(e)}"

    def updatecid(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            UPDATE tbl_cidade SET nome_cidade=?, Uf=?
            WHERE Cod_cidade=?
            """, (self.nome_cidade, self.Uf, self.Cod_cidade))
            banco.conexao.commit()
            c.close()
            return "Cidade atualizada com sucesso!"
        except Exception as e:
            c.close()
            return f"Ocorreu um erro na alteração da cidade: {str(e)}"

    def deletecid(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM tbl_cidade WHERE Cod_cidade=?", (self.Cod_cidade,))
            banco.conexao.commit()
            c.close()
            return "Cidade removida com sucesso!"
        except Exception as e:
            c.close()
            return f"Ocorreu um erro na remoção da cidade: {str(e)}"

    def selectcid(self, Cod_cidade):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM tbl_cidade WHERE Cod_cidade=?", (Cod_cidade,))
            row = c.fetchone()
            if row:
                self.Cod_cidade, self.nome_cidade, self.Uf = row
                c.close()
                return "Busca feita com sucesso!"
            else:
                c.close()
                return "Cadastro de cidade não encontrado."
        except Exception as e:
            c.close()
            return f"Ocorreu um erro na busca da cidade: {str(e)}"