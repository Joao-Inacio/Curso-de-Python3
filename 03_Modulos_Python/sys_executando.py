"""
    Sys.argv - Executando arquivos com argumentos no
sistema
"""
import sys
import os

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Faltando argumentos:')
    print('-a', 'Para lista todos os arquivos nesta pasta', sep='\t')
    print('-d', 'Para listar todos os diretórios nesta pasta', sep='\t')

so_arquivos = False
if '-a' in argumentos:
    so_arquivos = True

so_diretorios = False
if '-d' in argumentos:
    so_diretorios = True

for arquivo in os.listdir('.'):
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)

    if so_arquivos:
        if os.path.isdir(arquivo):
            print(arquivo)
