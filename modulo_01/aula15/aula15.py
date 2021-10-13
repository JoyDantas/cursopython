'''
Split, Join, Enumerate em Python
* Slipt = Dividir uma estring (str)
* Join = Unir uma lista (str)
* Enumerate = Enumerar elementos da lista (list/iteráveis)
'''

string = 'Brasil é o país do futebol, o Brasil é penta.'

lista = string.split(' ') # separando por espaço
lista_2 = string.split (',')

# print(lista)
# print(lista_2)

# for valor in lista:
#     print(f'A palavra "{valor}" apareceu {lista.count(valor)} vezes.')

# palavra = ''
# contagem = 0
#
# for valor in lista:
#     qtd_vezes = lista.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}X)')

for valor in lista_2:
    print(valor.strip().capitalize()) # strip remove o espaço do inicio e fim da string. Capitalize deixa maiusculo

### JOIN

string_01 = 'O Brasil é Penta.'
lista_03 = string_01.split(' ')
# string_02 = ','.join(lista_03) # junta por ','.
#
# print(string_02)

## Enumerate, função que retorna tuplas.

for indice, valor in enumerate(lista_03):
    print(indice, valor, lista_03[indice])

## Desempacotamento de lista


lista = ['Joys', 'Caroline','Dantas']
n1,n2, n3 = lista

print(lista)