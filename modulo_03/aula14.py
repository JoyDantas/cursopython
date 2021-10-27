"""
Geradores de arquivo

    As vezes esquecemos de dar um open() e close() na hora de trabalhar com arquivos. Pensando nisso o python permite criar suas proprias
    classes para resolver esse problema, onde não é necessário incluir close().

    Vamos ver as duas formas de trabalhar com geradores de arquivo.

"""

# 1 _ primeira forma

arquivo = open('ac.txt', 'w')
arquivo.write('Alguma coisa.')
arquivo.close()

## nesse primeiro exemplo precisamos definir open() e close().

# 2 Segunda forma sem close()

with open('ac.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')





