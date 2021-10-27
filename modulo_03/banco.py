class Banco:
    def __init__(self):
        self.agencias = [1111, 5555, 3333]
        self.cliente = []
        self.conta = []

    def add_cliente(self, cliente):
        self.cliente.append(cliente)

    def add_conta(self, conta):
        self.conta.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.cliente:
            return False

        if cliente.conta not in self.conta:
            return False

        if cliente.conta.agencia not in self.agencias:
            return False

        return True
