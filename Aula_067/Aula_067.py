# SETTER = CONFIGURANDO UM VALOR (=)
# GETTER = OBTER UM VALOR (.)
class Pessoa:
    def __init__(self):
        self.atributo = 'Inicial'

    @property
    def nome(self):
        return 'João Inácio'

    @nome.setter
    def nome(self, nome):
        self.atributo = nome


p1 = Pessoa()
print(p1.atributo)
print(p1.nome)  # Não se colocar parenteses
