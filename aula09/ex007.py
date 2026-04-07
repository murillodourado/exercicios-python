'''

Crie um algoritmo para solicitar 5 valores de itens comprados em um supermercado e mostre a soma total dos produtos comprados e o valor médio da compra

'''
lista_compras = []
soma = 0

for i in range(5):
    valor = float(input('Digite os valores dos produtos: '))
    lista_compras.append(valor)
    soma += valor

media = soma / 5

print(f'Lista dos valores dos produtos: {lista_compras}')
print(f'Média total dos valores: {media:.2f}')