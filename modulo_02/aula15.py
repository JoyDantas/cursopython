## reduce

from dados import produtos,pessoas,lista
from functools import reduce


## soma  total da lista e reduz em um unico número
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
print(soma_lista)

## acumulando os preços

soma_preco = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_preco/len(produtos)) ## achando a média dos produtos

## acumulando a idade e achando a média

soma_idade = reduce(lambda ac, i: i['idade'] + ac, pessoas, 0)
print(soma_idade/len(pessoas))