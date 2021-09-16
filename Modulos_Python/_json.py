"""
    JSON - JavaScript Object Notation
"""
from dados import *
import json

dados_json = json.dumps(clientes_dicionario)  # trasformando um dicionario para json


dicionario = json.loads(clientes_json)  # trasformando um json para dicionario

for chave, valor in dicionario.items():
    print(chave)
    print(valor)

# criando um arquivo json
with open('clientes.json', 'w') as arquivo:
    json.dump(clientes_dicionario, arquivo, indent=4)
"""
para ler um arquivo json e converte em um dicionario
with open('clientes.json', 'r') as arquivo:
    dados = json.loads(arquivo)
print(dados)
"""
