'''
ZIP - unindo iteráveis
ZIP_LONGEST - Itertools
'''

from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Rio de Janeiro', 'Laguna', 'Belo Horizonte', 'Salvador', 'Montes Claros']
estados = ['SP', 'RJ', 'SC', 'MG', 'BA']

# cidades_estados = zip(cidades,estados)
# print(dict(cidades_estados))
#
# ## zip une até a menor lista, por isso utilizamos o zip_longest para outros casos.
#
# cidades_estados = zip_longest(cidades,estados)
# print(dict(cidades_estados)) ## nesse caso ele preenche Montes Claros com none.
#
# cidades_estados = zip_longest(cidades, estados, fillvalue='Estado')
# print(dict(cidades_estados)) ## nesse caso, trocamos o none por 'Estado'.

cidades_estados = zip(
    indice,
    cidades,
    estados,
)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)
