from vendas.formata import preco


def aulmento(valor, porcentagem, formata=False):
    r = valor + (valor * (porcentagem / 100))
    if formata:
        return preco.real(r)
    else:
        return r


def reducao(valor, porcentagem, formata=False):
    r = valor - (valor * (porcentagem / 100))
    if formata:
        return preco.real(r)
    else:
        return r
