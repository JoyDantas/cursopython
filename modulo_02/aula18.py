'''
Lendo, escrevendo e apagando arquivos no Python
'''

## CRIANDO ARQUIVO

# file = open('abc.txt', 'w+')
# file.write('Linha 1\n')
# file.write('Linha 2\n')
# file.write('Linha 3\n')
# file.write('Linha 4\n')
#
# file.seek(0,0) ## buscando a posição no arquivo (onde o cursor estar) voltar ao topo do arquivo
# print('Lendo linhas: ')
# print(file.read())
# print('################################')
#
# file.seek(0,0)
# print(file.readline())
# print(file.readline())
# print(file.readline())
#
# print('################################')
# file.seek(0,0)
# for linha in file.readlines():
#     print(linha, end='')
#
# print('################################')
# file.seek(0,0)
# for linha in file:
#     print(linha)
#
# file.close()

## utilizando a maneira de contexto eu não preciso fechar o arquivo
#
# with open('abc.txt','w+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#
#     file.seek(0)
#     print(file.read())


## utilizando o r+ para ler os arquivos

# with open('abc.txt', 'r+') as file:
#     print(file.read())

## utilizando o a+: ele ativa o append mode (adiciona coisas ao arquivo)

# with open('abc.txt', 'a+') as file:
#     file.write('Outra linha\n')
#     file.seek(0)
#     print(file.read())

## apagando arquivo

# import os
# os.remove('abc.txt')

## lendo json

import json

d1 = {
    'Pessoa 1' : {
        'nome': 'Luiz',
        'idade' : 25,
    },
    'Pessoa 2' : {
        'nome' : 'Luisa',
        'idade': 30,
    },
}

d1_json = json.dumps(d1, indent=True)
with open('abc.json', 'w+') as file:
    file.write(d1_json)
