import sqlite3
class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        with self.conexao.cursor() as c:
            c.execute("""CREATE TABLE IF NOT EXISTS tbl_usuarios (
                idusuario INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT, 
                telefone TEXT, 
                email TEXT,
                usuarios TEXT,
                senha TEXT
            )""")
            self.conexao.commit()

    def createTable(self):
        c = self.conexao.cursor()
        try:
            c.execute("""
            CREATE TABLE IF NOT EXISTS tbl_cidades (
                idcidade INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                uf TEXT
            )
            """)

            self.conexao.commit()
        finally:
            c.close()
