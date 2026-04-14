'''

Crie um algoritmo para solicitar 5 nomes, idade. Após isso, envie as informações por pessoa em uma lista e deixe todas as informações em uma lista completa. Print a lista completa.

'''
lista_dados = []
i = 0

while i <= 5:
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    nome_idade = [nome, idade]
    lista_dados.append(nome_idade)
    i+= 1
    print(lista_dados)
