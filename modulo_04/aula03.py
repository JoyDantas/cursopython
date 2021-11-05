"""
Movendo, copiando e apagando arquivos com o OS e o SHUTIL
"""

import os
import shutil

# definindo caminho da pasta existente e caminho da pasta nova
pasta_origital = r'C:\Users\joys-\OneDrive\Documentos\Exames Rotina'
pasta_nova = r'C:\Users\joys-\OneDrive\Documentos\Exames Rotina2'

# bloco try, para criar nova pasta e trata excesão
try:
    os.mkdir(pasta_nova)
except FileExistsError as e:
    print(f'Pasta {pasta_nova} já existe.')

# caminhando pela pasta
for raiz, diretorios, arquivos in os.walk(pasta_nova):
    for arquivo in arquivos:
        arquivo_antigo_path = os.path.join(raiz, arquivo)
        arquivo_novo_path = os.path.join(pasta_nova, arquivo)

## movendo os arquivos para a nova pasta

        # shutil.move(arquivo_antigo_path, arquivo_novo_path)
        # print(f'Arquivos {arquivo} movidos com sucesso!')

## copiando arquivos entre pastas

        # shutil.copy(arquivo_antigo_path, arquivo_novo_path)
        # print(f'Arquivos {arquivo} copiado com sucesso!')

## apagando os arquivos

        os.remove(arquivo_novo_path)
        print('Arquivos apagados!')


