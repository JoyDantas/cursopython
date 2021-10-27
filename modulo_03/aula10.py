'''
Polimorfismo de sobreposição 

Polimorfismo é o principio que permite que classes derivadas de uma mesma superclasse tenham métodos iguais (de mesma assinatura)
mas com comportamentos diferentes. 

mesma assinatura = mesma quantidade e tipo de parâmetros. 

'''

from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def fala(self, msg):
        pass


class B(A):
    def fala(self, msg):
        print(f'B está falando {msg}')


class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')

b = B()
c = C()

b.fala('Um assunto.')
c.fala('Outro assunto.')