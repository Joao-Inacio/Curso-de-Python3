"""
    Deque - Trabalhando com LIFO e FIFO
"""
from collections import deque
"""fila = deque()
fila.append('João')
fila.append('Lucas')
fila.append('Maria')
fila.append('Luiz')
fila.append('Ana')
print(f'{fila.popleft()} Saiu')
print(f'{fila.popleft()} Saiu')
print(f'{fila.popleft()} Saiu')
print(f'{fila.popleft()} Saiu')
print(f'{fila.popleft()} Saiu')

for nome in fila:
    print(nome)"""
fila = deque(maxlen=5)
fila.extend([1, 2, 3, 4])
fila.append(5)
print(fila)
