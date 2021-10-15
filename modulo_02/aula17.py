'''
Módulo padrão do Python
Módulos são aquivos .py (contém código em python) e servem para expandir as funcionalidades
padrão da linguagem.

'''

import sys
print(sys.platform)

## importar 2 funções do mesmo modulo

from random import randint, random

## importar tudo que tem no módulo

from random import *

## quando o módulo não vem no python, podemos utilizar o pip para instala-lo exe: pymysql
## ir em terminal e digital 'pip install pymysql'

import pymysql

## se eu não precisar mais do modulo eu posso retira-lo do meu compuatador
## basta abrir novamente o terminal e digitar 'pip unistall pymysql' 