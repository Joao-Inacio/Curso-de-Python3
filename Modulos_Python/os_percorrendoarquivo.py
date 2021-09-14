"""
    OS - Percorrendo arquivos e pastas
"""
import os

caminho_procura = input('digite um caminho: ')
termo_procura = input('Digite um termo: ')


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'.replace('.', ',')


contador = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                contador += 1
                caminho_completo = os.path.join(raiz, arquivo)  # mostra o caminho completo
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
                print()
                print(f'Encontrei o arquivo: {arquivo}\n'
                      f'Caminho: {caminho_completo}\n'
                      f'Nome:{nome_arquivo}\n'
                      f'Extensão: {ext_arquivo}\n'
                      f'Tamanho: {tamanho}\n'
                      f'tamanho formatado: {formata_tamanho(tamanho)}')
            except PermissionError as e:
                print(f'Você não tem permição para ver esse arquivo: {arquivo}')
            except FileNotFoundError as e:
                print(f'Arquivo: {arquivo} não foi encontrado.')
            except Exception as e:
                print(f'Erro desconhecido: {e}')
print()
print(f'{contador} Arquivo(s) encontrado(s).')
