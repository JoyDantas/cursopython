# Índices
# 0123456789 .................33
# Iterando strings


frase = 'O rato roeu a roupa do rei de roma' # itarével

tamanho_frase = len(frase)
contador = 0
nova_string = ''
input_user = input('Qual letra vc deseja maiúscula: ')


# iterando
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_user:
        nova_string += input_user.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)