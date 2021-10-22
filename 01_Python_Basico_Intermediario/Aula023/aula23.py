"""
 Split, Join, Enumerate em Python
 * Dividir uma string
 * Join juntar uma lista
 * Enumerar elementos da lista
"""
str = "o Brasil é o país do futebol, o Brasil é penta."
lista = str.split(' ')
str2 = ','.join(lista)
'''
for valor in lista:
    print(f'A palavra {valor} apareceu {lista.count(valor)}x na frase') '''
palavra = ''
contagem = 0
for valor in lista:
    qtd_vezes = lista.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')
# print(str2)

for v1, v2 in enumerate(lista):
    print(v1, v2)

