"""
    Como criar pacotes e módulos em Python
"""
from vendas.calc_precos import aulmento
from vendas.formata import preco
preco1 = 49.90
preco_com_aumento = aulmento(valor=preco1, porcentagem=15, formata=True)
print(preco_com_aumento)
