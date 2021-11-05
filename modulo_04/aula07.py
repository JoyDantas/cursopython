"""
Trabalhando com arquivos em zip
"""

from zipfile import ZipFile
import os

#criando arquivo zip
caminho = r'C:\Users\joys-\OneDrive\Documentos\Exames Rotina'
with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)

#lendo arquivo zip
with ZipFile('arquivo.zip','r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

#extraindo zip

with ZipFile ('arquivo.zip', 'r') as zip:
    zip.extractall('descompactado')
