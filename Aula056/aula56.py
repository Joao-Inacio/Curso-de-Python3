"""
    Criando, lendo, escrevendo e apagando arquivos
"""
with open('abc.txt', 'w+') as file:
    file.write('linha 1\n')
    file.write('linha 2\n')
    file.write('linha 3\n')
    file.seek(0)
    print(file.read())

