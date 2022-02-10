c, q = input().split()
c = int(c)
q = int(q)
l = [4.00, 4.50, 5.00, 2.00, 1.50]
if c == 1:
    print(f'Total: R$ {l[0] * q:.2f}')
if c == 2:
    print(f'Total: R$ {l[1] * q:.2f}')
if c == 3:
    print(f'Total: R$ {l[2] * q:.2f}')
if c == 4:
    print(f'Total: R$ {l[3] * q:.2f}')
if c == 5:
    print(f'Total: R$ {l[4] * q:.2f}')
