## Operador ternário em Python

logged_user = True

# if logged_user:
#     print('Usuário logado.')
# else:
#     print('Usuário Precisa logar.')


# usando operador ternário

# msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'
# print(msg)

## segundo exemplo:

idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Precisa digitar apenas números')

idade = int(idade)

# if idade >= 18:
#     print('Pode acessar')
# else:
#     print('Não pode acessar')

msg = 'Pode acessar.' if idade >=18 else 'Não pode acessar.'

print(msg)

