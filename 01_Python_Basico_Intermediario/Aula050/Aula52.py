"""
    Uso de try e except como condicional
"""


def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass


numero = converte_numero(input('Digite um número: '))
if numero is None:
    print('Isso não é um número')
else:
    print(numero * 5)
