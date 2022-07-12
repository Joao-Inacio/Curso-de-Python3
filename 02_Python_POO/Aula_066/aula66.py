"""
    Encapsulamento - Python Orientado a Objetos
    _ protected(public _)
    __ private
"""


class BaseDeDados:
    def __init__(self):  # Construtor
        self.__dados = {}

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_clientes(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.inserir_clientes(1, 'João')
bd.inserir_clientes(2, 'Miranda')
bd.inserir_clientes(3, 'Rose')
bd.apaga_clientes(2)
bd.lista_clientes()
