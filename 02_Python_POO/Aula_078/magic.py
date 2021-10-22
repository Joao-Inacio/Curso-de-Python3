"""
    Métodos mágicos - Python Orientado a Objetos
"""


class A:
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)
        return super().__new__(cls)
        """

    def __init__(self):
        """print('Eu sou o INIT')"""
        pass

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)

    def __setattr__(self, key, value):
        self.__dict__[key] = value


a = A()
a.nome = 'João Inácio'
a(1, 2, 3, 4, 5, nome='Luiz')
