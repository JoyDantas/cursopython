'''
Aula - 13 Listas

fatiamento
funções append, insert, pop, del, clear, extend, +
min, max
range

'''

lista_1 = [1,2,3]
lista_2 = [4,5,6]

lista_3 = lista_1 + lista_2

lista_1.extend(lista_2)
lista_1.extend('a')
lista_2.append('b') # adiciona no final da lista.
lista_2.insert(0,'banana') # você escolhe em que posição adicionar na lista.
lista_2.pop() #exclui ultimo item da lista.

print(lista_1)
print(lista_2)
print(lista_3)

lista_4= [ 1,2,3,4,5,6,7,8,9]

print(lista_4)
del(lista_4[3:5]) #deletando um intervalo dentro da lista.
print(lista_4)
del(lista_4[0])# excluindo primeira posição.
print(lista_4)

print(max(lista_4)) # retorna valor máximo
print(min(lista_4)) # retorna menor valor


lista_5 = list(range(1,100,8))
print(lista_5)

soma = 0
for n in lista_5:
    soma += n
    print(f'{soma} + {n} = {soma}')
