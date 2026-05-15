# Criar um objeto contabancaria, depositar e sacar valores.

class contabancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

# Criando o objeto
conta = contabancaria('Murillo', 1500)

# Função para depositar
conta.depositar(2500)
conta.depositar(400)

print(conta.saldo)

# Função para sacar
conta.sacar(1000)
conta.sacar(200)

print(conta.saldo)