from Aula_073.eletronico import Eletronico


class Smartphone(Eletronico):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            print(f'{self._nome} não está ligado')
            return

        if self._conectado:
            print(f'{self._nome} Já está conectado.')
            return

        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            print(f'{self._nome} não está conectado.')
            return
        self._ligado = False


