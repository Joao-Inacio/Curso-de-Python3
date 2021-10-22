"""
O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.
Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""
from dataclasses import dataclass
from dataclasses import field


@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(
                f'Tipo Inválido {type(self.nome).__name__} != str em {self}'
            )

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('João', 'Inácio')
print(p1.nome, p1.sobrenome)

