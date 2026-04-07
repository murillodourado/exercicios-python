'''

Crie um algoritmo para acumular os 5 valores que o usuário poderá inserir. Ao final, retorne a lista e a soma destes valores.

'''
lista_numeros = []
soma = 0

for i in range(5):
    numero = int(input('Digite os números: '))
    lista_numeros.append(numero)
    soma += numero

print(lista_numeros)
print(f'A soma é {soma}')