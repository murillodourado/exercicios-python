'''

Crie um algoritmo que simule um menu, a qual a opção 1, solicita nome, opção 2, solicita cpf, opção 3, solicite idade, opção 4, sai da estrutura.

'''
lista_nomes = []
lista_cpf = []
lista_idade = []

while True:
    entrar_menu = int(input('''
    Digite uma opção para entrar em algum menu:\n
    1 (Para nome)\n
    2 (Para cpf)\n
    3 (Para idade)\n
    4 (Para sair) 
    '''))

    if entrar_menu == 1:
        nome = input('Digite seu nome: ')
        lista_nomes.append(nome)
    elif entrar_menu == 2:
        cpf = input('Digite seu CPF: ')
        lista_cpf.append(cpf)
    elif entrar_menu == 3:
        idade = int(input('Digite sua idade: '))
        lista_idade.append(idade)
    elif entrar_menu == 4:
        break

print(lista_nomes)
print(lista_cpf)
print(lista_idade)