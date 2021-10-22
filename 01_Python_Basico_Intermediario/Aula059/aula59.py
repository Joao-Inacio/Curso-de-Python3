"""
    Problema dos parâmetros mutáveis em funções
"""
'''
    Mutável: Lista, Dicionários
    Imutável: Tuplas, strings, números, True, False, None
'''


def list_client(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


list_client_1 = ['Fabrício']
client1 = list_client(['João', 'Maria', 'Eduardo'], list_client_1)
client2 = list_client(['Marcos', 'Jonas', 'Zico'])
client3 = list_client(['Jose'])

print(client1)
print(client2)
print(client3)

