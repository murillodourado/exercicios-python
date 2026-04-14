''''

Utilizando while, crie um algoritmo para solicitar 5 carros para o usuário e insira em uma lista

'''

lista_carros = []
i = 1

while i <= 5:
    carro = input('Digite uma marca de carro: ')
    lista_carros.append(carro)
    i+= 1
    print(lista_carros)