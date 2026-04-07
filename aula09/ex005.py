'''

Crie um algoritmo para solicitar 6 valores inteiros e separe estes números em duas listas: lista par e lista ímpar. Print as duas listas.

'''
lista_par = []
lista_impar = []

for i in range(6):
    numero = int(input('Digite os números: '))
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

print(f'Lista dos números pares: {lista_par}')
print(f'Lista dos números ímpares: {lista_impar}')