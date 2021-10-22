"""
     OS + SHUTIL - Mover, copiar e apagar arquivos
"""
import os
import shutil

caminho_original = r'C:\Users\joaoi\Videos\teste1'
novo_caminho = r'C:\Users\joaoi\Videos\teste2'

try:
    os.mkdir(novo_caminho)
except FileExistsError as e:
    print(f'Pasta {novo_caminho} já existe')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(novo_caminho, file)

        # shutil.move(old_file_path, new_file_path) Para mover arquivos
        if '.txt' in file:
            shutil.copy(old_file_path, new_file_path)
            print(f'Arquivo {file} copiador com sucesso')
        """
        if '.srt' in file:  para apagar um arquivo
            os.remove(new_file_path)
        """

