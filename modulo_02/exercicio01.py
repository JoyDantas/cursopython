'''
1) Crie uma função que exibe uma saudação os parâ,etros saudação e nome.
2) Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
3) Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex: 10%).
Retorne (return) o vakir di oruneuri búmero somado do aumento do percentual do mesmo.
4) Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne fizz, se o parâmetro for divisível por 5 retorne buzz.
Se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado.
'''

#1)
def saudas(saudacao,nome):
    print(f'{saudacao} {nome}!!')

print(saudas('Olá', 'João'))

#2)

def soma(n1,n2,n3):
    print(n1+n2+n3)

soma(1,1,3)
soma(1,6,3)


#3) aumento percentual

def aumento_percentual(n1,n2):
    return n1 + (n1 * n2 / 100)

print(aumento_percentual(50,10))
print(aumento_percentual(10,30))
print(aumento_percentual(100,10))
print(aumento_percentual(15,100))

#4) Fizz Buzz

def fb(n):
    if n % 3 == 0 and n % 5 ==0:
        return'FizzBuzz'
    if n % 5 == 0:
        return 'Buzz'
    if n % 3 ==0:
        return 'Fizz'
    return n

print(fb(15))
print(fb(26))
print(fb(9))
print(fb(10))
