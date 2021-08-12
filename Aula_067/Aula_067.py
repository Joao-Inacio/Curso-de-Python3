# SETTER = CONFIGURANDO UM VALOR (=)
# GETTER = OBTER UM VALOR (.)
class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property  # GETTER
    def nome(self):
        return self._nome  # Não se use assim self.nome no GETTER e no SETTER Loop

    @nome.setter  # SETTER
    def nome(self, nome):
        self._nome = nome


p1 = Pessoa('João')
p1.nome = 'Otávio'
print(p1.nome)  # Não se colocar parenteses
