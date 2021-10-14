# listas, tuples, str -> Sequences ou Iterável
## iteradores e geradores são feitos para consumir seus valores uma unica vez

nome = 'Joys Dantas'
iterador = iter(nome)

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

