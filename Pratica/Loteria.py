from random import sample

gera_Numero = sorted(sample(range(1, 26), 15))
acumulado = 1.50000000
print('*/' * 25, 'Lotofácil', '*/' * 25)
print('Acumulado: R$ 1.500.000,00\n'
      'Escolha 15 número de 01 a 25')
n = 1
numeros_usuario = []
while len(numeros_usuario) < 15:
    numeros = int(input(f'{n}° Número: '))
    numeros_usuario.append(numeros)
    n += 1

    if len(numeros_usuario) == len(set(numeros_usuario)):
        continue

    else:
        print('Numero já adicionado')
        numeros_usuario.remove(numeros)
        n -= 1

num = set(gera_Numero).intersection(numeros_usuario)
num_acertado = 0
for s in num:
    num_acertado += 1

print(f' Os números sorteados foram {gera_Numero}\n'
      f' Você apostou nos números {numeros_usuario}\n '
      f'Você acertou {num_acertado} números \n')
if num_acertado < 10:
    print('Que pena não foi dessa vez, mais sorte na proxima')
elif num_acertado == 11:
    print('!!!Parabéns!!! Você ganhou R$ 5.00')
elif num_acertado == 12:
    print('!!!Parabéns!!! Você ganhou R$ 10.00')
elif num_acertado == 13:
    print('!!!Parabéns!!! Você ganhou R$ 25.00')
elif num_acertado == 14:
    print(f'!!!Parabéns!!! Você ganhou R$ {acumulado * 0.2:.2f}')
elif num_acertado == 15:
    print(f'!!!Parabéns!!! Você ganhou R$ {acumulado}')
