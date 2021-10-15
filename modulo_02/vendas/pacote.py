from formata import real

def aumenta(valor, porcentagem,formata=False):
    resultado = valor + (valor * (porcentagem / 100))

    if formata:
        return real.formata_real(resultado)
    else:
        return  resultado

def diminui (valor, porcentagem,formata=False):
    resultado = valor - (valor * (porcentagem / 100))

    if formata:
        return real.formata_real(resultado)
    else:
        return resultado

