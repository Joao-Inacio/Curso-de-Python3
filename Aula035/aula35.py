"""
Sistema de perguntas e respostas com dicionários em
Python
"""
perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanta é 2 + 2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '5',
        },
        'resposta_certa': 'b',
    },
    'pergunta 2': {
        'pergunta': 'Quanta é 3 * 2?',
        'respostas': {
            'a': '5',
            'b': '10',
            'c': '6',
        },
        'resposta_certa': 'c',
    },
}
print()

resposta_certa = 0
for pk, pv in perguntas.items():
    print(f"{pk}: {pv['pergunta']}")

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('EHHHH!!! Você acertou!!!')
        resposta_certa += 1
    else:
        print('XIIIII!!! Você errou!!')

    print()
qtd_perguntas = len(perguntas)
pct_acerto = resposta_certa / resposta_certa * 100

print(f'Você acertou {resposta_certa} respostas')
print(f'Sua porcentagem de acerto foi de {pct_acerto}%')
