n = int(input())
l = []
for i in range(1, n + 1):
    x = input().split()
    a, b, c = x
    l.append(((float(a) * 2 + float(b) * 3 + float(c) * 5) / 10))

print(f'{l[0]:.1f}')
print(f'{l[1]:.1f}')
print(f'{l[2]:.1f}')
