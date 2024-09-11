from Banco import Banco

class LoginModel:
    def _init_(self):
        self.banco = Banco()

    def buscar_usuario(self, idUsuario):

        try:
            usuario_encontrado = self.banco.buscar_usuario(idUsuario)

            if usuario_encontrado:
                print(f"Usuário encontrado: {usuario_encontrado}")
                return usuario_encontrado
            else:
                print("Usuário não encontrado.")
                return None
        except Exception as e:
            print(f"Ocorreu um erro ao buscar o usuário: {e}")
        return None