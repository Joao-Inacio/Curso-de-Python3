"""
crie uma função1 que receba uma função 2 como parâmetro e retorne o valor da função 2 executada
"""


def func1():
    print(func2())


def func2():
    return 'eai'


func1()

# Resolunção

def ola_mundo():
    return 'olá mundo!'


def mestre(funcao):
    return funcao()


exec = mestre(ola_mundo)
print(exec)
