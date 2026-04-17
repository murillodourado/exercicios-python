'''

Crie um algoritmo para ignorar números negativos. se numero < 0 continue, se numero = 0 break, traga a lista de numeros

'''
lista_numeros = []

while True: 
    numero = int(input('Digite um número: '))

    if numero < 0:
        continue
    elif numero == 0:
        break
    else:
        lista_numeros.append(numero)

print(f'Lista sem números negativos: {lista_numeros}')