"""
    Polimorfismo é o principio que permitir que classes derivadas de uma mesma superclasse tenha métodos iguais
    (de mesma  assinatura) mas comportamentos diferntes.
    Mesma assinatura = Mesma quantidade e tipo de parâmetros
"""
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def fala(self, msg): pass


class B(A):
    def fala(self, msg):
        print(f'B etá falando {msg}')


class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')


b = B()
c = C()
b.fala('Um assunto')
c.fala('Outro')
