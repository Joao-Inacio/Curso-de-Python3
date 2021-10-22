"""
    Metaclasses
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        if 'b_fala' not in namespace:
            print(f'Você precisa criar o método b_fala em {name}')

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def fala(self):
        self.b_fala()


class B(A):
    pass
