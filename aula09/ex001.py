# Estrutura de repetição (for)
lista_final = []


for n in range(10):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))

    nome_idade = [nome, idade]
    lista_final.append(nome_idade)
    print(lista_final)
