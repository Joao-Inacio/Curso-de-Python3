idade = []
while True:
    i = int(input())
    idade.append(i)
    if i <= 0:
        idade.remove(i)
        break
me = sum(idade)
print(f'{me / len(idade):.2f}')
