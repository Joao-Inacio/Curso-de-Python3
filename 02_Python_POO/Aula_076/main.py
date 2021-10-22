"""
    Criando Exceções - Python Orientado a Objetos
"""


class TaErradoError(Exception):
    pass


def testar():
    raise TaErradoError('Errado!')

try:
    testar()
except TaErradoError as error:
    print(f'Erro:{error}')
