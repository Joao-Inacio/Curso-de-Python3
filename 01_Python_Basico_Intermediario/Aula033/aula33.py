"""
Tuplas
"""
t1 = 1, 2, 3, 'a', 'b'
t2 = 6, 7, 8, 9, 10
t3 = t1 + t2

n1, n2, n3, *_ = t3

print(n3)
print(type(t1))

t1_lis = list(t1)
t1_lis[1] = 3000
print(t1_lis)
