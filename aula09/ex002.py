'''

Crie um algoritmo para solicitar 5 números. Após isso, insira os 5 números em uma lista e print a lista final.

'''
lista_numeros = []

for n in range(5):
    numero = int(input('Digite os números que deseja: '))
    lista_numeros.append(numero)

print(lista_numeros)