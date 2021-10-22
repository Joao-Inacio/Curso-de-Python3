"""
Comportamento de geradores e iteradores
"""
nome = 'João Inácio'
iterador = iter(nome)

try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
except:
    pass

print('Faltou')
for valor in iterador:
    print(valor)
