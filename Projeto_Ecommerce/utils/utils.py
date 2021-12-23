def qtd_total_carr(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])
