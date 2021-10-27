from pessoa import Banco, Conta, Cliente, ContaCorrente, ContaPoupanca, ABC, abstractmethod

banco = Banco()

cliente1 = Cliente('José Ricardo', 31)
cliente2 = Cliente('Julia Maria', 26)
cliente3 = Cliente('Ana Ferreira', 45)

conta1 = ContaCorrente(4521, 4678, 0)
conta2 = ContaPoupanca(7521, 8578, 0)
conta3 = ContaPoupanca(1564, 4811, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente2)
banco.inserir_cliente(cliente2)

banco.inserir_cliente(cliente3)
banco.inserir_conta(cliente3)

if banco.autenticar(cliente2):
    cliente2.conta.depositar(20)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado.')

print("********************************")

if banco.autenticar(cliente3):
    cliente3.conta.depositar(0)
    cliente3.conta.sacar(50)
else:
    print('Cliente não autenticado.')
