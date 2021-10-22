"""
Funções def = return
"""


def f(var):
    print(var)


def dumb():
    return f


# var = dumb()()
dumb()('Colocar valor')
