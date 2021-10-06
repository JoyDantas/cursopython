## CONDIÇÕES IF,ELIF, ELSE

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

idade_lim = 18

idade_menor = 20 # muito jovem
idade_maior = 30 # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} Pode receber emprestimo')
else:
    print(f'{nome}  Não pode receber emprestimo. ')

# OPERADORES LÓGICOS OR, AND, NOT , IN E NOT IN

usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Joys'
senha_bd = 'D@antas22'

if usuario_bd == usuario and senha_bd == senha:
    print('Usuário logado.')
else:
    print('Senha ou usuário inválido. Tente Novamente')
