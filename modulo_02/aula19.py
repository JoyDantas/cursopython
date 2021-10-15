## funções decoradoras

from time import time
from time import sleep

def velocidade (funcao):
    def interna (*args, **kwargs):
        start_time = time()
        resultado = funcao(*args,**kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000 ## milesegundos
        print(f'\n A função {funcao.__name__},'
            f' levou {tempo:.2f}ms para ser executada.')
        return resultado
    return interna

@velocidade
def demora():
    for i in range(500):
        print(i, end='')

demora()