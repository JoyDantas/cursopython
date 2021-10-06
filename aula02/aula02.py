## f strings formatação de strings

nome = 'Joys'
idade = 25
altura = 1.59
peso = 52
imc = peso/(altura**2)

print(nome, 'tem', idade,'de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e o seu imc é de {imc:.2f}')

## formatando com o formate
print('{} tem {} anos de idade e seu imc é de {:.2f}'.format(nome,idade,imc))

## Exercício

nome = 'Joys'
idade = 25
altura = 1.60
peso = 52
ano_atual = 2021
ano_nascimento = ano_atual - idade
imc = peso/(altura**2)

print(f'Me chamo {nome}, tenho {idade} de idade. \nMinha altura é {altura} e meu peso é {peso}.\nNasci no ano de {ano_nascimento} e meu imc é {imc:.2f}')