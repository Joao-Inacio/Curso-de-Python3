i = []
while True:
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x > y:
        i.append('Decrescente')
    if x < y:
        i.append('Crescente')
    if x == y:
        break
for e in i:
    print(e)
