n = 0
v = 1
while v <= 6:
    nu = float(input())
    if nu >= 0:
        n += 1
    v += 1
print(f'{n} valores positivos')