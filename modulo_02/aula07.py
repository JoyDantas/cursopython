## compreensão de dicionário

lista = [
    ('chave','valor'),
    ('chave2','valor2'),
]

d1 = {x:y for x,y in lista}
d2 = {x:y*2 for x,y in lista}
d3 = {x.upper(): y.upper() for x,y in lista}

print(d1)
print(d2)
print(d3)
