import PyPDF2
import os

## Unindo PDFS

## caminho que o arquivo está no PC
caminho = r'C:\Users\joys-\OneDrive\FIAP'

novo_pdf = PyPDF2.PdfFileMerger()
# caminha pelo arquivo
for root, dirs, files in os.walk(caminho):
    for file in files:
        caminho_completo = os.path.join(root, file)

        arquivo_pdf = open(caminho_completo, 'rb')
        novo_pdf.append(arquivo_pdf)

with open(f'{caminho}/novo_arquivo.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)


