##Dicionarios


d1 = {'chave1':'valor da chave '}
d1['nova_chave'] = 'valor da nova chave'

print(d1['nova_chave'])

# outra forma de fazer dicionários
d2 = dict(chave2='valor da chave 2', chave3= 'valor da outra chave 3')
print(d2)

## Em dicionário toda chave deve ser única.

d1.update({'chave':'novo_valor'}) #adiciona  novo valor no dicionário.
print(d1)

del d1['chave'] # apaga um valor no dicionário.
print(d1)

print('valor da chave 2' in d2.values()) #achar valores no dicionário.
print('chave2' in d2.keys()) #acha chave no dicionário.

print(len(d2)) #conta a quantidade de pares no dicionario (chave e valor).

# iterando com dic

#vendo valor
for k in d2.values():
    print(k)

#vendo chave e valor
for k in d2.items():
    print(k[0],k[1])

# dic maior

clientes = {
    'cliente1': {
        'Nome': 'Luiz',
        'Sobrenome' : 'Souza',
    },
    'Cliente2': {
        'Nome':'João',
        'Sobrenome' : 'Pereira',
    },
    'Cliente3': {
        'Nome':'Joys',
        'Sobrenome': 'Dantas',
    },
 }

for c, n in clientes.items():
    print(f'Exibindo {c}')
    for dados_k, dados_v in n.items():
        print(f'\t{dados_k} = {dados_v}')

copia = clientes.copy() # fazer cópia
print(copia)

#concatenar dicionários
# p/ concaternar dicionários o sinal de + não funciona! em seu lugar utilizamos o update

d1.update(d2)
print(d1)