i = int(input())
qtd_dias = [365, 12, 30]
resul = []
for n in qtd_dias:
    qtd = int(i / n)
    print(f'{qtd}ano(s)'
          f'{qtd} mes(es)'
          f'{qtd} dia(s)')
    i -= qtd * n