## pass, ..., segurando o lugar para escrever posteriormente sem erros

#1)

'''
Faça um programa que peça um número inteiro, informe se este número é par ou impar.
Caso o user não digite um número inteiro, informe que não é inteiro.
'''

num = input('Digite um número: ')

if num.isdigit():
    num = int(num)
    if num % 2 ==0:
        print(f'{num} é par!')
    else:
        print(f'{num} é ímpar!')
else:
    print('Isso não é um número inteiro!')


'''
Faça um programa que pergunte a hora e baseando-se no horário descrito,
exiba a saudação apropriada. 
Ex : 0-11 bom dia, 12 - 17 boa tarde e 18-23 boa noite
'''

# 2)

hora = input('Digite um horário (0-23): ')

if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('Horário deve estar entre 0 e 23')
    else:
        if hora <= 11:
            print('Bom Dia!')
        elif hora <= 17:
            print('Boa Tarde!')
        else:
            print('Boa Noite!')


'''
Faça um código que peça o primeiro nome do user. Se o nome tiver 4 letras imprima 'seu nome é curto',
se o nome tiver entre 5 e 6 letras, imprima 'seu nome é normal' e seu for maior que 6 imprima 
'seu nome é muito grande'.
'''
#3)

nome = input('Digite seu nome: ')
qtd_nome = len(nome)

if qtd_nome <= 4:
    print('Seu nome é curto.')
elif qtd_nome <=6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
