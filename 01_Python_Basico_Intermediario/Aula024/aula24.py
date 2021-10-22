"""
Desempacotamento de lista em python
"""
lista = ['Luiz', 'João', 'Maria', 10, 20, 50, 100]
n1, n2, *outra_lista, ultimo_valor = lista
print(n1, outra_lista, ultimo_valor)
