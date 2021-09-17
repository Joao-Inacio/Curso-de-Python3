"""
    CSV - Comma Separated Values
"""
import csv
"""
with open('clientes.csv', 'r') as arquivo:
    dados = csv.reader(arquivo)  # csv.DictReader(arquivo)
    next(dados)

    for dado in dados:
        print(dado)  # print(dado['nome'], dado['sobrenome'])
"""

with open('clientes.csv', 'r',  newline='') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]

"""- para acessar o laço de fora
for dado in dados:
    print(dado)
"""
with open('clientes2.csv', 'w',  newline='') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )
    """ print(dados[0].keys())"""

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
