'''
public, protected e private

Python:
_ privado/ protected (publico)
__ privado(_NOMECLASSE__nomeatributo)

'''

class BaseDeDados:
    def __init__(self):
        self.__dados = []

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id:nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id,nome)

    def apaga_clientes(self,id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()

bd.inserir_cliente(1,'Joys')
bd.inserir_cliente(2,'Ana')
bd.inserir_cliente(3,'João')
bd.inserir_cliente(4,'Carol')
bd.apaga_clientes(3)
bd.lista_clientes()

