from hashlib import new


class Pessoa:
    def __init__(self):
        self.__nome = ''
        self.__idade = ''
        self.__sexo = ''

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo


p1 = Pessoa()
p1.nome = 'joao'
p1.sexo = 'M'
p1.idade = 23 
print(p1.nome)
print(p1.idade)
print(p1.sexo)
