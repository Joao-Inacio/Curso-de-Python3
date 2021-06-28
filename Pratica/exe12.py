"""
Uma função que receba uma função 2 como parâmetro e retorne o valor da função 2 executada faça a função um executar
duas função que receba um número diferente de argumentos
"""


# Deu tudo errado
"""
def func1():
    print(func2())


def func2():
    return func2()


func1()"""


# Solução

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def see_hi(nome):
    return f'Oi {nome}'


def saud(nome, saudacao):
    return f'{saudacao} {nome}'


execu = mestre(see_hi, 'Luiz')
print(execu)
