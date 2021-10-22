"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não Importa
Permutaçâo - ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations
pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']
for grupo in permutations(pessoas, 2):
    print(grupo)
