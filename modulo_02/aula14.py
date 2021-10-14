# filter

from dados import produtos, pessoas, lista

## filtrando utilizando a função filter

nova_lista = filter(lambda x:x >= 5,lista)
print(list(nova_lista))

## também é possível fazer o mesmo com list compreshetion

nova_lista2 = [x for x in lista if x >= 5]
print(nova_lista2)

## agora vamos pegar produtos maiores que 10,00

maior_dez = filter(lambda p:p['preco'] > 60, produtos)

for produto in maior_dez:
    print(produto)

## também podemos criar uma função para utilizar um filtro mais complexo

def filtrando(produto):
    if produto['preco'] > 50:
        return True
    else:
        return False

nova_lista3 = filter(filtrando, produtos)

for produto in nova_lista3:
    print(produto)

### filtrando quem tem mais que 25 anos

nova_idade = filter(lambda i:i['idade'] >= 25 and i['idade'] <= 50, pessoas)

for pessoa in nova_idade:
    print(pessoa)

