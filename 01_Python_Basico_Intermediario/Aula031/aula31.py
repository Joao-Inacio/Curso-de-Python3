"""
escopo de variavel
"""
variavel = 'valor'


def func():
    print(variavel)


def func2():
    global variavel  # não é uma boa pratica
    variavel = 'Outro valor'
    print(variavel)


func()
func2()
print(variavel)
