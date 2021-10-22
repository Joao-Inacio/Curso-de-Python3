class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} Falando')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} esta comprando')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} esta estudando')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        super().falar()  # Ou Pessoa.falar(self)
        print(f'{self.nome} {self.sobrenome} Outra coisa')
