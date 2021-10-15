import os
import shutil


nome_do_arquivo = input('Nome do arquivo + extenção: ')
caminho_original = r'C:\cursoPython\Pratica'
novo_caminho = r'C:\Users\joaoi\OneDrive\Documentos\my-lab\Curso-de-Python3\Pratica'
arquivo_original = fr"{caminho_original}\{nome_do_arquivo}"

try:
    os.mkdir(arquivo_original)
except FileExistsError as e:
    print(f'Arquivo {arquivo_original} não existe')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(novo_caminho, file)

        if nome_do_arquivo in file:
            shutil.copy(old_file_path, new_file_path)
            print(f'Arquivo {file} copiador com sucesso')
