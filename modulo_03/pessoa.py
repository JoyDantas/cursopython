from abc import ABC, abstractmethod


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

        def inserir_conta(self, conta):
            self.conta = conta


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self.agencia}\n')
        print(f'Conta: {self.conta}\n')
        print(f'Saldo: {self.saldo}\n')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo Insuficiente.')
            return

        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

        def sacar(self, valor):
            if (self.saldo + self.limite) < valor:
                print('Saldo Insuficiente.')
                return

            self.saldo -= valor
            self.detalhes()


class Banco:
    def __init__(self):
        self.agencia = [1111, 5555, 3333]
        self.cliente = []
        self.conta = []

    def inserir_cliente(self, cliente):
        self.cliente.append(cliente)

    def inserir_conta(self, conta):
        self.conta.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.cliente:
            return False
        if cliente.conta not in self.conta:
            return False
        if cliente.conta.agencia not in self.agencia:
            return False
        return True
