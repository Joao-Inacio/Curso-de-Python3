"""nota = []
nv = []
while True:
    n1 = float(input())
    n2 = float(input())
    if n1 >= 0 and n1 <= 10:
        nota.append(n1)
    if  n2 >= 0 and n2 <= 10:
        nota.append(n2)
    if n1 < 0 or n2 < 0 or n1 > 10 or n2 > 10:
        nv.append('nota invalida')
    if len(nota) == 2:
        break
for i in nv:
    print(i)
print(f'media = {sum(nota) / 2:.2f}')"""
nota_valida = 0
x=0
media=0
while nota_valida!=2:
    x = float(input())
    if x>=0 and x<=10:
        media+=x/2
        nota_valida+=1
    else:
        print('nota invalida')


print(f'media = {media}')
