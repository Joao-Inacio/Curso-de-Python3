# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         return super().__call__(*args, **kwargs)


# class Pessoa:
#     def __new__(cls, *args, **kwargs):
#         return super().__new__(cls)

#     def __init__(self, nome):
#         self.nome = nome

#     def __call__(self, x, y):
#         print('Call chamado', self.nome, x, y)


# p1 = Pessoa('João')
# p1(2, 2)
# print(p1.nome)

class Singleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.tema = 'O tema escuro'
        self.font = '18px'


if __name__ == '__main__':
    as1 = AppSettings()
    as2 = AppSettings()
    as1.tema = 'O tema claro'

    print(as1.tema)
    as2 = AppSettings()
    print(as1.tema)
    print(as2.tema)
