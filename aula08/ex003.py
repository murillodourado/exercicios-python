'''

Verificar senha do usuário, porém, crie variáveis para as condições

'''

senha_cadastrada = '12345'

pedir_senha = input('Digite sua senha: ')

verificar_senha = senha_cadastrada == pedir_senha

if verificar_senha == True:
    print('Senha correta!')
else:
    print('Senha incorreta')