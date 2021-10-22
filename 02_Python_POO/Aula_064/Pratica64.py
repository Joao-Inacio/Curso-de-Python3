
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, porcento=50):
        self.preco = self.preco - (self.preco * (porcento / 100))

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor


produto1 = Produto('Bola', 25)
produto1.desconto()
print(produto1.nome, produto1.preco)
