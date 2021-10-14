## sistema de perguntas e respostas em dicionários

perguntas = {
    'Pergunta 1':{
        'pergunta':'Quanto é 5 * 2 ?',
        'resposta':{'a':'1','b':'5','c':'10'},
        'resposta_certa': 'c'
    },
    'Pergunta 2':{
        'pergunta':'Quanto é 4 * 2 ?',
        'resposta':{'a':'8','b':'6','c':'100'},
        'resposta_certa': 'a'
    },
    'Pergunta 3':{
        'pergunta':'Quanto é 8 + 4 ?',
        'resposta':{'a':'-8','b':'2','c':'12'},
        'resposta_certa': 'c'
    },
    'Pergunta 4':{
        'pergunta':'Quanto é 20 / 2 ?',
        'resposta':{'a':'10','b':'2','c':'20'},
        'resposta_certa': 'a'
    },
    'Pergunta 5':{
        'pergunta':'Quanto é 3 * 3 ?',
        'resposta':{'a':'6','b':'9','c':'10'},
        'resposta_certa': 'b'
    },
}
print ()
resposta_certa = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv["resposta"].items():
        print(f'[{rk}]: {rv}')

    resposta_user = input('Digite sua resposta: ')

    if resposta_user == pv['resposta_certa']:
        print('EHHHHHH, Você acertou!')
        resposta_certa += 1

    else:
        print('XIIIII, Você errou! :(')

    print ()

qtd_acertada = len(perguntas)
porcentagem_certa = resposta_certa / qtd_acertada * 100

print(f'Você acertou {resposta_certa} respostas.')
print(f'Seu percentual de acerto foi de {porcentagem_certa}%.')

