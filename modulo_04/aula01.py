# Trabalhando com datas no Python


from datetime import datetime  # para pegar as datas
from locale import setlocale, LC_ALL  # para trabalhar com formatação em pt
from calendar import mdays  # para pegar a quatidade de dias do mês

setlocale(LC_ALL, "pt_BR.utf-8")

dt = datetime.now()  # data atual
mes_atual = int(dt.strftime("%m"))
formatacao1 = dt.strftime("%A, %d de %B de %Y")
formatacao2 = dt.strftime("%d/%m/%Y")
hora = dt.strftime("%H:%M:%S")
formatacao3 = dt.strftime("%d-%m-%Y")
formatacao4 = dt.strftime("%A,%d de %Y")

print(formatacao1)
print(formatacao2)
print(hora)
print(formatacao3)
