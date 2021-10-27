"""
O que são dataclasses?

O módulo Dataclasses fornece um decorador e funcções para criar automaticamente métodos, como o __init__(), __repr__(),
__eq__() e etc. Em classes definidas pelo usuário. Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PED 557.
Adicionado na versão 3.7 do Python.

"""

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

p1 = Pessoa('Joys', 'Dantas')
print(p1.nome)
print(p1.sobrenome)
print(p1.nome_completo())

