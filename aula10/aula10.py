'''

While em Python

utilizado para realizar ações enquanto uma condição for verdadeira.
requisitos: entender  condições e operadores.

while = enquanto for verdadeiro
'''


## com iteração para sair do laço infinito

## continue
## break

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+, - , * , /)')
    sair = input('Deseja sair? [s] Sim ou [n] Não. ')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '*':
        print(num_1 * num_2)
    elif operador == '/':
        print(num_1 / num_2)
    else:
        print('Operador inválido')
print('acabou!')

