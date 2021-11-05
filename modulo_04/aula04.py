"""
Trabalhando com JSON

JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas e programas leve e de fácil
utilização. Muito utilizado em APIS
"""

import json

## criando um dicionario em python

cliente_dicionario = {
    1: {
        'nome': 'Joys Dantas',
        'idade': 26,
        'altura': 1.60,
        'peso': 52.50,
    },
    2: {
        'nome': 'Paulo Henrique',
        'idade': 60,
        'altura': 1.80,
        'peso': 82.50,
    },
    3: {
        'nome': 'Camila Prado',
        'idade': 36,
        'altura': 1.50,
        'peso': 62.50,
    },
}

print(cliente_dicionario)

"""
DUMPS / Dump
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None
"""

# Transformando o dicionario em json
# útil para salvar informações de qualquer tipo
dados = json.dumps(cliente_dicionario, indent=4)  ## indent permite visualizar melhor
print(dados)  ## formato json

# Converter json em dicionario
# util para carregar informações de qualquer tipo

dados = json.loads(cliente_json)
print(dados)

#exportando dicionário para arquivo json

with open('clientes.json','w') as file:
    json.dump(cliente_dicionario, file, indent=4)

#importando string de um arquivo json e converte em dicionario
with open('clientes.json','r') as file:
    data = json.load(file)

print(data)