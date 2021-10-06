## desempacotando listas em python

lista = ['Ana','Paula', 'Fernando',4,5,6,8,7]

n1,n2,n3, *nome_variavel = lista

print(n1,n2,n3)
print(nome_variavel)