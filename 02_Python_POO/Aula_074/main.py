"""
    Classes Abstratas - Python Orientado a Objetos
"""

from classes.contapoupança import ContaPoupanca
from classes.contacorrente import ContaCorrente


cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)
print('#'*45)
cc = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=500)
cc.depositar(100)

