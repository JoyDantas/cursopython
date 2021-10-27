'''
Associação - Usa | Agregação - Tem | Compisição - É dono | Herança - É
'''

from aula07_2 import Pessoa, Cliente, Estudante

c1 = Cliente('José Antonio', 28)
c1.falar()
c1.comprar()

e1 = Estudante('Henrique Lima', 18)
e1.falar()
e1.estudar()

p1 = Pessoa('Ana Motta', 31)
p1.falar()