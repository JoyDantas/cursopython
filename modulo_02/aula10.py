'''
count - itertools
'''

from types import GeneratorType

variavel = zip('alo','alo')
# print(list(variavel))

print(next(variavel))
print(next(variavel))
print(next(variavel))

## transformando em um gerador

v = ((x,y) for x,y in zip('alo','alo'))
print(isinstance(v, GeneratorType))

## Contador me retorna um iterador

from itertools import count

contador = count(start=5, step=0.5)

# print(next(contador))
# print(next(contador))
# print(next(contador))

## cuidado com laços infinitos

for valor in contador:
    print(round(valor,2))

    if valor >= 10:
        break


## criando um contador com 2 linhas 
c = count()
lista = ['ana', 'fernando', 'henrique', 'marcela', 'ricardo']

lista = zip(c, lista)
print(list(lista))