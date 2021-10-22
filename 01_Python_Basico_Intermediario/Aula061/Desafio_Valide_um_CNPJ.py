import Aula061.cnpj as cnpj

cnpj_sem = cnpj.remover_caract('00.000.000/0000-00')
n1 = 6
lista1 = []
for i in cnpj_sem[:12]:
    n1 -= 1
    if n1 == 1:
        n1 = 9
    c = int(i) * n1
    lista1.append(c)
n2 = 7
lista2 = []
for i in cnpj_sem[:13]:
    n2 -= 1
    if n2 == 1:
        n2 = 9
    c = int(i) * n2
    lista2.append(c)

res1 = sum(lista1)

digit1 = 11 - (res1 % 11)

if digit1 > 9:
    digit1 = 0

res2 = sum(lista2)

digit2 = 11 - (res2 % 11)

if digit2 > 9:
    digit2 = 0

if str(digit1) == cnpj_sem[12] and str(digit2) == cnpj_sem[13]:
    print(f'O Seu Cnpj {cnpj_sem} é válido')
else:
    print('Cnpj inválido')
