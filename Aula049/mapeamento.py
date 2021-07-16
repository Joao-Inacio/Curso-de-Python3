from aula49 import produtos, pessoas, lista


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


precos = map(aumenta_preco, produtos)

for produto in precos:
    print(produto)

print()

nomes = map(lambda p: p['nome'], pessoas)
for pessoa in nomes:
    print(pessoa)

print(lista)

