"""
Sistema de perguntas e respostas com dicionários em
Python
"""
perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanto é 5 x 5?',
        'respostas': {
            'a': '5',
            'b': '15',
            'c': '25',
            'd': '55',
        },
        'resposta_certa': 'c',
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 5 + 5?',
        'respostas': {
            'a': '5',
            'b': '15',
            'c': '25',
            'd': '10',
        },
        'resposta_certa': 'd',
    },
    'pergunta 3': {
        'pergunta': 'Quanto é 25 - 5?',
        'respostas': {
            'a': '20',
            'b': '15',
            'c': '25',
            'd': '10',
        },
        'resposta_certa': 'a',
    },
    'pergunta 4': {
        'pergunta': 'Quanto é 50 / 100?',
        'respostas': {
            'a': '1',
            'b': '10',
            'c': '2',
            'd': '50',
        },
        'resposta_certa': 'c',
    },
    'pergunta 5': {
        'pergunta': 'Quanto é 5 x 5?',
        'respostas': {
            'a': '5',
            'b': '15',
            'c': '25',
            'd': '55',
        },
        'resposta_certa': 'c',
    },
    'pergunta 6': {
        'pergunta': 'De quem é a famosa frase “Penso, logo existo”??',
        'respostas': {
            'a': 'Platão',
            'b': 'Galilei Galilei',
            'c': 'Descartes',
            'd': 'Sócrates',
        },
        'resposta_certa': 'c',
    },
    'pergunta 7': {
        'pergunta': 'De onde é a invenção do chuveiro elétrico?',
        'respostas': {
            'a': 'França',
            'b': 'Brasil',
            'c': 'Australia',
            'd': 'Itália',
        },
        'resposta_certa': 'b',
    },
    'pergunta 8': {
        'pergunta': 'Quantas casas decimais tem o número pi?',
        'respostas': {
            'a': 'Duas',
            'b': 'Centenas',
            'c': 'Vinte',
            'd': 'Infinitas',
        },
        'resposta_certa': 'd',
    },
    'pergunta 9': {
        'pergunta': 'Atualmente, quantos elementos químicos a tabela periódica possui?',
        'respostas': {
            'a': '113',
            'b': '109',
            'c': '118',
            'd': '92',
        },
        'resposta_certa': 'c',
    },
    'pergunta 10': {
        'pergunta': 'O que a palavra legend significa em português?',
        'respostas': {
            'a': 'Legenda',
            'b': 'Lenda',
            'c': 'Legendário',
            'd': 'História',
        },
        'resposta_certa': 'b',
    },
}
print()

respostas_certas = 0
respostas_erradas = 0
qtd_erros = 3
for pk, pv in perguntas.items():
    print(f'Tentativas {qtd_erros}')
    print(f"{pk}: {pv['pergunta']}")

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('EEEHHHHHH!!! Você acertou!!')
        respostas_certas += 1
        qtd_perguntas = len(perguntas)
        if respostas_certas == qtd_perguntas:
            qtd_perguntas = len(perguntas)
            pct_acertos = respostas_certas / qtd_perguntas * 100
            print(f'Sua porcentagem de acerto foi de {pct_acertos}%')
            print(f'Você acertou {respostas_certas} Respostas de {qtd_perguntas} perguntas')
    else:
        print('XIIII!!! Você errou!!')
        qtd_erros -= 1
        respostas_erradas += 1
        if respostas_certas >= 1:
            qtd_perguntas = len(perguntas)
            pct_acertos = respostas_certas / qtd_perguntas * 100
            print(f'Sua porcentagem de acerto foi de {pct_acertos}%')
            print(f'Você acertou {respostas_certas} Respostas de {qtd_perguntas} perguntas')
        if qtd_erros <= 0:
            print('Opa!! Você perdeu todas as tentativas')
            break



