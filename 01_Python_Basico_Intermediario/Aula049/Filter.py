from aula49 import produtos, pessoas, lista

nova_lista = filter(lambda x: x >= 5, lista)
# ou
'''
nova_lista = [x for x in lista if x > 5]
'''
print(list(nova_lista))


def filtra(produto):
    if produto['preco'] > 50:
        return True


nova_lista2 = filter(filtra, produtos)

for produto in nova_lista2:
    print(produto)
print()

def filtra_p(pessoa):
    if pessoa['idade'] >= 45:
        return True


nova_lista3 = filter(filtra_p, pessoas)

for pessoa in nova_lista3:
    print(pessoa)
