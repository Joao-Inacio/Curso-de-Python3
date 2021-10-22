"""
Zip e Zip_longest - Unindo iteráveis
"""
from itertools import zip_longest, count
indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Mulungu']
estados = ['SP', 'MG', 'BA', 'CE']

cidades_estados = zip(indice, estados, cidades)

'''
print(next(cidades_estados))
print(next(cidades_estados))
print(next(cidades_estados))
print(next(cidades_estados))
'''
# ou
for valor in cidades_estados:
    print(valor)

# Zip_longest

cidades2 = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Mulungu', 'Rio de Janeiro']
estados2 = ['SP', 'MG', 'BA', 'CE']

cidades_estados2 = zip_longest(indice, estados2, cidades2, fillvalue='Estado')
'''print(list(cidades_estados2))'''


