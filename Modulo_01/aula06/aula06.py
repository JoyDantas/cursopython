usuario = input('Digite seu user: ')
qtd_carac = len(usuario)

print(usuario, qtd_carac, type(qtd_carac))

if qtd_carac < 6:
    print('Falta caracter, minimo 6 caracter')
else:
    print('Você foi cadastrado no sistema')

