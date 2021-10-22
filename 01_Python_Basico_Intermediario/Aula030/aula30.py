"""
Funções (def) - *args **kwargs
"""


# def func(a1, a2, a3, a4, a5, nome=None, a6=None):
#     print(a1, a2, a3, a4, a5, nome, a6)
def func(*args, **kwargs):
    print(args, kwargs)


lista = [1, 2, 3, 4, 5]
func(*lista, nome='João')
