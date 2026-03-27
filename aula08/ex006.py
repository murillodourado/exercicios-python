'''

Crie um algoritmo para solicitar senha, idade e acesso e mostre que o usuário apenas quando todas as informações forem verdadeiras
crie variáveis para as condições

'''
acesso = input('Você quer acessar?(Sim) ou (Não)?: ').lower()
acesso_sim = acesso == 'sim'

if acesso_sim == True:
    print('Você acessou o sistema!')
    idade = int(input('Digite sua idade: '))
    idade_valida = idade >= 18

    if idade_valida == True:
        print('Idade permitida!')
        senha = input('Digite sua senha: ')
        senha_valida = senha == '12345'

        if senha_valida == True:
            print('Senha válida! Você acessou o sistema!')
        else:
            print('Senha inválida!')
    else:
        print('Idade não permitida!')
else:
    print('Você não acessou o sistema!')