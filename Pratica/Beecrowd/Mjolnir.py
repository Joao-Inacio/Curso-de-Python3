n = int(input())
for i in range(1, n + 1):
    nome, forca = input().split()
    if nome == "Thor" or int(forca) > 25000:
        print('Y')
    else:
        print('N')