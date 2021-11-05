## Módulo Random

import random

# gera um número inteiro entre A e B.
import string

inteiro = random.randint(10, 20)

# gera um número aleátorio com a função range()
inteiro1 = random.randrange(900, 1000, 10)

# gera um número flutuante entre A e B.
flutuante = random.uniform(10, 20)

# gera um número flutuante entre 0 e 1
flutuante1 = random.random()

# sorteio de lista
#seleciona aleátoriamente valores em uma lista
lista = ['Luiz', 'Maria', 'Mario', 'Felipe', 'Ana', 'João', 'Zé']
sorteio = random.choice(lista)
sorteio1 = random.choices(lista, k=2)
sorteio2 = random.sample(lista, 2)

#embaralha a lista
random.shuffle(lista)

#gera senha aleatória
letra = string.ascii_letters
digitos = string.digits
caracteres = '@!#$%&*'
gera = letra + digitos + caracteres
senha = ''.join(random.choices(gera, k=15))
print(senha)

print(sorteio)
print(sorteio1)
print(sorteio2)
print(inteiro)
print(flutuante)
print(flutuante1)
print(inteiro1)
