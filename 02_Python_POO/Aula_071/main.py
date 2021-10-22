"""
    Herança Simples - Python Orientado a Objetos
    Associação = Usa
    Agregação = Tem
    Composição = É dono
    Herança = É
"""
from Aula_071.classes import *

c1 = Cliente('Luiz', 45)
print(c1.nome, c1.idade)
c1.falar()
c1.comprar()
a1 = Aluno('Maria', 54)
print(a1.nome, a1.idade)
a1.falar()
a1.estudar()
