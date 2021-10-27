from cp import ContaPoupanca
from cc import ContaCorrente

cp = ContaPoupanca(7452, 4585, 100)
cp.depositar(10)
cp.sacar(100)
cp.sacar(10)
cp.sacar(5)

print('***************************')

cc = ContaCorrente(agencia=7544, conta=8954, saldo=450, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(250)
cc.sacar(250)
cc.depositar(200)
cc.sacar(150)