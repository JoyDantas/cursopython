# OPERADORES LÓGICOS OR, AND, NOT , IN E NOT IN

usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Joys'
senha_bd = 'Dantas22'

if usuario_bd == usuario and senha_bd == senha:
    print('Usuário logado.')
else:
    print('Senha ou usuário inválido. Tente Novamente')