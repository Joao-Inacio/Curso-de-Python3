import re


def remover_caract(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)




