n = int(input())
for i in range(0, n):
    x, y = input().split()
    x = int(x)
    y = int(y)
    try:
        print(x / y)
    except:
        print('divisao impossivel')