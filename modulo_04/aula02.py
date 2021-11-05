"""
Trabalhando com o sistema OS - Percorrendo arquivos e pastas
Nesse código vamos criar formas de achar determinado arquivo no computador com o OS que identifica caminhos
"""

import os

caminho_procura = input(r'Digite um caminho: ')
termo_procura = input("Digite um termo: ")
conta = 0


## bloco para formatação de tamanho de arquivo com um metódo

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

    ## tratando as casas decimais
    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'.replace('.', ',')


## utilizando o OS com o metodo walk, ele caminha por todas as pastas
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)
                print()
                print('Encontrei o Arquivo:', arquivo)
                print("Caminho: ", caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', ext_arquivo)
                print('Tamanho: ', tamanho)
                print('Tamanho Formatado', formata_tamanho(tamanho))
            ## tratamento de exceções
            except PermissionError as e:
                print('Sem Permissão')
            except FileExistsError as e:
                print('Arquivo não Encontrado')
            except Exception as e:
                print('Erro Desconhecido:', e)
print()
print(f'{conta} arquivo(s) encontrado(s).')
