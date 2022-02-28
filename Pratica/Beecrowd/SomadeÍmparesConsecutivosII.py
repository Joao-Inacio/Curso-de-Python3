l = []
while True:
    x, y = input().split()
    x = int(x)
    y = int(y)
    if x > y:
        l.append('Decrescente')
    else:
        l.append('Crescente')

for i in l:
    print(i)