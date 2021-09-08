"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""

from banco import Banco
from clientes import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cli1 = Cliente('João', 22)
cli2 = Cliente('Ana', 18)
cli3 = Cliente('Pedro', 48)

con1 = ContaPoupanca(1111, 123456, 0)
con2 = ContaCorrente(2222, 654321, 0)
con3 = ContaPoupanca(1212, 987654, 0)

cli1.inserir_conta(con1)
cli2.inserir_conta(con2)
cli3.inserir_conta(con3)

banco.inserir_cliente(cli1)
banco.inserir_conta(con1)

if banco.autenticar(cli1):
    cli1.conta.depositar(50)
    cli1.conta.sacar(25)
else:
    print('Cliente não autenticado')

print('#'*50)

if banco.autenticar(cli2):
    cli2.conta.depositar(50)
    cli2.conta.sacar(25)
else:
    print('Cliente não autenticado')



