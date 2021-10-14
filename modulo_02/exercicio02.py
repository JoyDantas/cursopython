'''
1 - Crie uma função 1 que receba uma função 2 como parâmetro e retorne o valor da função 2 executada
2 - Crie uma função 1 que receba uma função 2 como parâmetro e retorne o valor da função 2 executada. Faça a funçao 1
    executar duas funçoes que recebam um número diferente de argumentos.

'''

#1)
def func1 ():
    return 'Olá Mundo!'

def func2 (funcao):
    return funcao()

executando = func2(func1)
print(executando)

#2)

def mestre(funcao,*args,**kwargs):
    return funcao(*args,**kwargs)

def fala_oi (nome):
    return f'Oi {nome}'

def saudacao (nome,saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, 'Joys')
executando2 = mestre (saudacao, 'Joys', saudacao='Bom dia!')

print(executando)
print(executando2)