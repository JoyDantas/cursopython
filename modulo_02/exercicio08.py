'''
Considerando duas listas de inteiros ou floats ( lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

exemplo:

lista_a = [ 1,2,3,4,5,6,7]
lista_b = [1,2,3,4]

resultado

lista_soma = [2,4,6,8]
'''

lista_a = [44, 6, 4, 5, 2, 8]
lista_b = [1, 2, 3, 4]

#lista_soma = []

#1)

# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# 2)
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b [i])
# print(lista_soma)

#3

lista_soma = [ x + y for x,y in zip(lista_a, lista_b)]
print(lista_soma)