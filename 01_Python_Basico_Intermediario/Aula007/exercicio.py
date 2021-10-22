
nome = 'Paulo Oliveira'
idade = 30
altura = 1.79
peso = 85
ano_atual = 2021
imc = peso / (altura * altura)
ano_nascimento = ano_atual - idade
print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}.\n'
      f'O IMC de {nome} é {imc:.2f}.\n'
      f'{nome} nasceu em {ano_nascimento}.')

