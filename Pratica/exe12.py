"""
Uma função que receba uma função 2 como parâmetro e retorne o valor da função 2 executada faça a função um executar
duas função que receba um número diferente de argumentos
"""


def func1():
    print(func2())


def func2():
    return func2()


func1()
