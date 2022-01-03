n = int(input())
qtd_segundos = [3600, 60, 1]
result = []

for num in qtd_segundos:
    qtd = int(n / num)
    result.append(str(qtd))
    n -= qtd * num

print(':'.join(result))
