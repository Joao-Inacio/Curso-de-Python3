"""
    Random - números aleatórios e mais
"""
import random
import string

inteiro = random.randint(10, 20)
# gerar um número float de A e B
flutuante = random.uniform(10, 20)

lista = ['1', '2', '3', '4', '5']
sorteio = random.choice(lista)
"""sorteio = random.choices(lista, k=2)"""
sorteio_dupla = random.sample(lista, 2)

""" random.shuffle(lista) """
# gera senha aleatórias
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*()_-+=[{}]'
geral = letras + digitos + caracteres
passw = "".join(random.choices(geral, k=64))

print(passw)
