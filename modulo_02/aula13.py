# Função map

 ## importando dados


from dados import produtos,pessoas,lista

## alterando a lista com a função map
nova_lista = map(lambda x:x * 2, lista)
print(list(nova_lista))
print(lista)

## também conseguimos fazer o mesmo com list compresention

nova_lista1 = [valor * 2 for valor in lista]
print(nova_lista1)

## chegamos no mesmo resultado que a função map só que utilizando apenas uma linha de código

## agora vamos acrescentar 5% no preço dos produtos com map ()

# 1) primeiro vamos criar um dicionário só com os preços

print('***************************************************************')
precos = map(lambda p: p['preco'], produtos)

for preco in precos:
    print(preco)

## 2) agora vamos definir uma função para aumentar o preco

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05,2) # para arrumar as casas decimais utilizamos o round e definimos a quantidade de casas, no caso 2.
    return p

novos_produtos = map(aumenta_preco, produtos)

for produto in novos_produtos:
    print(produto)


print('********************************************************')

idade = map(lambda i: i['idade'] * 1.20, pessoas)

for idade in idade:
    print(idade)


def aumeta_idade(i):
    i['idade'] = round(i['idade'] * 1.20)
    return i


nova_idade = map(aumeta_idade, pessoas)


for idade in nova_idade:
    print(idade)