"""
Expressões lambda - funçoes anônimas
"""
a = lambda x, y: x * y

print(a(2, 2))


lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

lista.sort(key=lambda item: item[1])
print(lista)  # Ou print(sorted(lista, key=lambda i: I[1], reverse=True))
