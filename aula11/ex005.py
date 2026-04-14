''''

Crie um algoritmo para simular fatorial a partir do valor inserido pelo usuário.

'''

numero = int(input('Digite valor de n: '))

fat = 1
i = 1

while i <= numero: 
    fat *= i
    i += 1
    # print(fat)

print(fat)