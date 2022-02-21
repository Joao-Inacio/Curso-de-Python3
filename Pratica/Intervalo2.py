n = int(input())
c = 1
i = 0 
o = 0
while c <= n:
    x =int(input())
    if x >= 10 and x <= 20:
        i += 1
    else:
        o += 1
    c += 1

print(f'{i} in')
print(f'{o} out')
