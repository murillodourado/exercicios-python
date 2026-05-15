# Com base no exercício anterior, crie uma conta para Julia, sabendo que ela tem 1500 de saldo inicial, e depois fez 2 depósitos, 1. R$ 250,00 ; 2. R$150,00. Após um tempo, ela sacou 100 reais para pagar um almoço no shopping. Qual é o saldo na conta da Julia?

class contabancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor} realizado!')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado')
        else:
            print('Saldo insuficiente!')

# Criando a conta da Julia
conta = contabancaria('Julia', 200)

# Input para depositar
deposito1 = float(input('Digite o valor do primeiro depósito: '))
deposito2 = float(input('Digite o valor do segundo depósito: '))

# Fazendo os depósitos
conta.depositar(deposito1)
conta.depositar(deposito2)

# Input para saque
saque1 = float(input('Digite o valor do saque: '))

# Fazendo o saque
conta.sacar(saque1)

# Mostrando saldo final
print(f'Saldo final da conta da {conta.titular}: R${conta.saldo}')