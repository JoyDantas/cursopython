
from pacote import *
from formata import real


preco = 49.9
preco_aumentado = aumenta(preco,15,formata=True)
print(preco_aumentado)

preco_diminui = diminui(preco,15,formata=True)
print(preco_diminui)