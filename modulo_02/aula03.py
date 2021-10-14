## Funções Lambda, funções anonimas.
## Sempre que precisarmos passar uma função para outra função e tivermos muito código, podemos usar uma função anonima lambda.
a = lambda x,y: x*y
print(a(4,2))


lista = [
    ['p1', 13],
    ['p2', 8],
    ['p3', 3],
    ['p4', 50],
]

lista.sort(key=lambda item: item[1], reverse=True) ## ordenando lista com lambda.
print(lista)

print(sorted(lista,key=lambda i:i[1]))