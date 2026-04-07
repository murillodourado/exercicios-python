'''

Crie um algoritmo para solicitar 5 nomes. Após isso, insira os 5 nomes em uma lista e print cada nome de forma separada com uma estrutura de textos: O nome é: nome

'''
lista_nomes = []

for nome in range(5):
    nome = input('Digite o nome que deseja: ')
    lista_nomes.append(nome)
    print(f'O nome é: {nome}')

print(f'Lista final: {lista_nomes}')