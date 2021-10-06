'''
Formantando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. (NÚMERO)f - Quantidade de casas decimais (float) :.f
: (CARACTERE) (> ESQUERDA < DIREITA OU ^ CENTRO) (TIPO - s, d ou f)
'''

nome = 'joys Caroline dantas'

print(nome.lower()) # tudo minusculo
print(nome.upper())# tudo maiusculo
print(nome.title())# primeira letras maiuscula

num_1 = 3
num_2 = 7

divisao = num_2/num_1

print(divisao)
print(f'{divisao:.2f}')
print(f'{num_1:0>10}')
print(f'{num_1:*<10}')
print(f'{num_1:#^10}')

num_3 = 1530

print(f'{num_3:0<5}')
print(f'{num_3:.2f}')

