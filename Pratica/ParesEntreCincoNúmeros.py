"""
beecrowd | 1065
Pares entre Cinco Números
"""
n = 0
v = 1
while v <= 5:
    nu = int(input())
    if nu % 2 == 0:
        n += 1
    v += 1
print(f'{n} valores pares')
