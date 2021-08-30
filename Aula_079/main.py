"""
    Context Manager - Criando e Usando gerenciadores de
    contexto
"""
from contextlib import contextmanager


"""
class Arquivo:
    def __init__(self, arquivo, modo):
        print('Iniciou a classe')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('entrou na classe')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('fechou a  classe')
        self.arquivo.close()


with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('\nAlguma\n ')
"""


@contextmanager
def abrir(arquivo, modo):
    try:
        print('Iniciou arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('fechou arquivo')
        arquivo.close()


with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
