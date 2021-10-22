"""
Formatando valores com modificadores
:s - Texto (str)
:d - Inteiro (int)
:f - número (float)
:.(NÚMERO) f - quantidade de casas decimais (float)
:(CARACTERE)(> ou < ^)(QUANTIDADE)(TIPO - s, d ou f )

> - Esquerda
< - Direita
^ - Centro

"""

num1 = 1
print(f'{num1:0>10}')
n1 = 10
n2 = 3
d = n1 / n2
print('{:.2f}'.format(d))
