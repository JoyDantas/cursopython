## groupby
from itertools import groupby

alunos = [
    {'nome': 'Ana', 'nota': 'A'},
    {'nome': 'Pedro', 'nota': 'B'},
    {'nome': 'Luiz', 'nota': 'C'},
    {'nome': 'Fernanda', 'nota': 'A'},
    {'nome': 'Mariana', 'nota': 'A'},
    {'nome': 'Julio', 'nota': 'D'},
    {'nome': 'Silvio', 'nota': 'C'},
    {'nome': 'Joaquim', 'nota': 'B'},
    {'nome': 'Amanda', 'nota': 'B'},
    {'nome': 'Joys', 'nota': 'A'},
    {'nome': 'Barbara', 'nota': 'B'},
]

# metódo

def ordena(item):
    return item['nota']

## sort (ordenando) os alunos

alunos.sort(key=ordena)

alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    valores = list(valores_agrupados)

    print(f'Agrupamento: {agrupamento}')

    for aluno in valores:
        print(f'\t {aluno}')

    quantidade = len(valores)
    print(f'\t{quantidade} alunos tiraram nota {agrupamento}')