"""
Exercícios proposto
"""
carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

total = sum([float(y) for x, y in carrinho])
# total = {x: y+y for x, y in carrinho}


print(total)

