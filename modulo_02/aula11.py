'''
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - ordem importa e repete valores únicos
'''

## combinações possiveis
from itertools import combinations
pessoas = ['luiz','leticia', 'amanda','ricardo','rose','fabricio']

for grupo in combinations(pessoas,2):
    print(grupo)

## quando a ordem importa utilizar os permutations (fabricio e luis vs luis e fabricio)

from itertools import permutations

print('####################################')

for grupo in permutations(pessoas,2):
    print(grupo)

print('####################################')

# se eu quero todas as combinações e a ordem importa utilizar o product ex: (fabricio e fabricio)

from itertools import product

for grupo in product(pessoas, repeat=2):
    print(grupo)

print('####################################')

