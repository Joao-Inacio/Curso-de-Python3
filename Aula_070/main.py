"""
    Composição - Python Orientado a Objetos
    Relação mais forte entre as classes
"""
from Aula_070.classes import Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
print()

cliente2 = Cliente('Mariar', 55)
cliente2.insere_endereco('Salvado', 'BA')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('João', 22)
cliente3.insere_endereco('Mulungu', 'CE')
print(cliente3.nome)
cliente3.lista_enderecos()
print()
