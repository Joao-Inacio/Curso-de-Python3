n = int(input())
cs = [100, 50, 20, 10, 5, 2, 1]
print(n)
for c in cs:
    qtd_cs = int(n / c)
    print(f'{qtd_cs} nota(s) de R$ {c},00')
    n -= qtd_cs * c

