
lista = [
    [1,2,3,5,6,7,8,9,4,5],
    [5,6,9,7,2,3,4,5,6,1],
    [1,5,4,5,6,3,2,8,9,7],
    [2,3,6,5,6,1,4,7,8,9],
    [8,9,4,5,4,7,8,5,6,1],
    [5,6,1,7,8,9,5,4,5,7],
    [6,3,5,2,8,7,4,1,2,8],
    [7,4,5,6,5,4,7,9,8,4],
    [1,2,5,4,3,6,5,7,8,9],
    [5,4,7,8,9,5,4,2,6,8],
    [8,5,9,7,8,5,9,8,4,5],

]
def encontra_primeiro (paramentro_inteiros):
    num_checados = set()
    primeiro_duplicado = -1

    for numero in paramentro_inteiros:
        if numero in num_checados:
            primeiro_duplicado = numero
            break

        num_checados.add(numero)
    return primeiro_duplicado

for lista  in lista:
    print(encontra_primeiro(lista))
