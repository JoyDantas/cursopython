'''
Funções (def) em Python - *arg e ** kwargs

 '''

def func(*args, **kwargs): #args é utilizado quando não sabemos a quantidade de argumentos passados na função. kwargs são argumentos nomeados
    print(args) # para os argumentos
    print(kwargs) # para os nomes/chaves

    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print('não tem idade')

lista = [1,2,3,4,5,6]
lista2 = [10,20,30]
func(*lista, *lista2, nome='José', sobrenome='Silva',idade=30)
# print(*lista, sep='_') ##podemos utilizar o * para desempacotar listas e o sep é um argumento da função print

