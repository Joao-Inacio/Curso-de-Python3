try:
    nome = input('Qual é seu nome: ')
    tamanho = len(nome)
    if tamanho <= 4:
        print(f'{nome} Seu nome é curto')
    elif 5 <= tamanho <= 6:
        print(f'{nome} Seu nome é normal')
    else:
        print(f'{nome} Seu nome é muito grande')

except:
    print('Algo deu errado')

