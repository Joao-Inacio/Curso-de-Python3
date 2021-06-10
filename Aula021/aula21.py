"""
Lista em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
lista1 = [0, 1, 2, 3, 4]
lista2 = [5, 6, 7, 8, 9]

# lista1.append('b')
# lista2.insert(0, 'Uva')

# lista3 = lista1 + lista2
# print(f'{lista1} + {lista2} = {lista3} ')
# lista2.pop()
# print(lista2)
# del(lista1[2:5])
# print(lista1)
# l1 = list(range(0, 11))
# for n in l1:
#     print(n)
secreto = 'perfume'
digitadas = []
chances = 3
while True:
    if chances <= 0:
        print('Você Perdeu!!')
        break
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahh isso não vale, digite apenas uma letra.')
        continue
    digitadas.append(letra)
    if letra in secreto:
        print(f'Quente, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Frio, a letra "{letra}" Não Existe na palavra secreta.')
        digitadas.pop()
    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    if secreto_temporario == secreto:
        print(f'Parabens você ganhou!!! a palavra é {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')
    if letra not in secreto:
        chances -= 1
    print(f'Você ainda tem {chances} chances.\n')

