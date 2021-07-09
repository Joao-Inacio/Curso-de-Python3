
carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

# total = [(x, y) for x, y in carrinho]
# total = {x: y+y for x, y in carrinho}
total = 0
soma = {x: y+y for x, y in carrinho}

print(soma)

