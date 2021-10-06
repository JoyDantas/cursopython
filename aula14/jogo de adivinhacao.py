secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <=0:
        print('VOCÊ PERDEUUUUU!')
        break

    letra = input('Digite um letra: ')

    if len(letra) > 1:
        print(" Ahhh isso não vale. Digite apenas uma letra. ")
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Uhullllll, a letrs "{letra}" EXISTE na palavra secreta.')
    else:
        print(f'AFFZZZ, a letra "{letra}" não EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Que legal!!!, VOCÊ GANHOU O GAME!!! a palavra secreta era "{secreto}".')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
        print(f'Você ainda tem {chances} chances.')
        print()