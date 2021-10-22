"""
Dicionário em python
"""
"""
d1 = dict(chave1='valor da chave', chave2='valor da outra chave')
d1 = {'chave1': 'valor da chave'}
 """
d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla',
}
v = d1.copy()  # cria uma copia rasa

d1.update({'nova_chave': 'novo_valor'})
'''
del d1['str']
'''

if d1.get('str') is not None:
    print(d1.get('str'))

print(d1, v)
