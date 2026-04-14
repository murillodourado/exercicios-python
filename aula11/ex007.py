'''

Crie um algoritmo para solicitar valor de produtos de um supermercado para o usuário, caso o usuário digite 0, sai da estrutura. Ao final, traga o valor total da compra

'''

total = 0

valor = float(input("Digite o valor do produto (0 para sair): "))

while valor != 0:
    total += valor
    valor = float(input("Digite o valor do produto (0 para sair): "))

print("Total da compra:", total)