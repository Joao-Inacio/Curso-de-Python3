"""
    Agregação - Python Orientado a Objetos
"""
from Aula_069.classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camiseta', 50)
p2 = Produto('Iphone', 8250)
p3 = Produto('Caneca', 15)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.lista_produtos()

print(carrinho.soma_total())
