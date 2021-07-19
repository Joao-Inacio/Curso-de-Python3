"""
    Try, Except - Tratando Exceções em Python
"""
try:
    a = {}
    print(a[1])
except NameError as erro:
    print('Error', erro)
except (IndexError, KeyError) as erro:
    print('Erro de índice ou Chave')
except Exception as erro:
    print('Ocorreu um erro inesperado.')
finally:
    print('Finalmente')
print('cheguei até aqui')
