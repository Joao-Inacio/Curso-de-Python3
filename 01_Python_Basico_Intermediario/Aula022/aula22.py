"""
For / Else em Python
"""
variavel = ['Joõa', 'Ana', 'Mateus']

for valor in variavel:
    if valor.lower().startswith('j'):
        print('Começa com J', valor)
    else:
        print('Não começa com J', valor)
