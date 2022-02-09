from typing import List, Union, Tuple, Dict, NewType, Callable, Sequence, \
    Iterable

# Primitivos
numero: int = 10
flutuan: float = 10.5
booleano: bool = False
string: str = 'João Inacio'

# Sequências
lista: List[int] = [1, 2, 3, 4, 5]
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'João']
tupla: Tuple = (1, 2, 3)

# Meu tipo
MeuDict = Dict[str, Union[str, int, List[int]]]  # Alias

# Dicionários e Conjuntos
pessoa: Dict[str, Union[int, str]] = {'nome': 'João', 'sobrenome': 'Inácio',
                                    'idade': 23}
pess2: Dict[str, Union[str, int, List[int]]] = {
    'nome': 'João', 'sobrenome': 'Inácio', 'idade': 23, 'l': [1, 2]}
pess3: MeuDict = {'nome': 'joão',
                    'sobrenome': 'Inácio', 'idade': 23, 'l': [1, 2]}

# Meu outro tipo
UserId = NewType('UserId', int)
user_id = UserId(325456789)


def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao


def soma(x: int, y: int) -> int:
    return x + y


print(retorna_funcao(soma)(10, 20))


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando...')


def iterar(sequencia: Sequence[int]):
    return [x for x in sequencia]


def iterar2(sequencia: Iterable[int]):
    return [x for x in sequencia]


print(iterar([1, 2, 3]))
print(iterar((1, 2, 3)))
print(iterar2([1, 2, 3]))
print(iterar2((1, 2, 3)))
