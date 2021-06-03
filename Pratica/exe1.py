try:
    print(50 * '#')
    print('Verificador de Número Ímpares e Pares')
    print(50 * '#')
    nu = int(input('Digite um número: '))
    if (nu % 2) == 0:
        print(f'{nu} É um número Par')
    else:
        print(f'{nu} É um número Ímpar')
except:
    print('Algo deu errado tente colocar um número inteiro')


