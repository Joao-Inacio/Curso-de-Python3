"""
PyPDF2 - Unindo e dividindo arquivos PDF
"""
import os

import PyPDF2

caminho_dos_pdfs = r'C:\Users\joaoi\OneDrive\Documentos\pdf'
"""
novo_pdf = PyPDF2.PdfFileMerger()
for root, dirs, files in os.walk(caminho_dos_pdfs):
    for file in files:
        caminho_completo_arquivo = os.path.join(root, file)
        arquivos_pdf = open(caminho_completo_arquivo, 'rb')
        novo_pdf.append(arquivos_pdf)

with open(fr'{caminho_dos_pdfs}\novo_arquivo.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)
"""
with open(r'C:\Users\joaoi\OneDrive\Documentos\pdf\novo_arquivo.pdf', 'rb') as arquivos_pdf:
    leitor = PyPDF2.PdfFileReader(arquivos_pdf)
    num_paginas = leitor.getNumPages()

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(fr'C:\Users\joaoi\OneDrive\Documentos\pdf\{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)

