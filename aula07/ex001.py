'''
1 - Sistema de login com nível de acesso. solicite usuário e senha. Se usuário é igual a admin,
crie uma estrutura de condição aninhada para solicitar senha e se a mesma for '1234', 
mostre que o usuário terá acesso total. Caso o usuário insira a senha incorreta, 
mostre senha incorreta. Caso usuário insira usuário incorreto, mostre usuário incorreto.
'''

usuario = input('Usuário: ')

senha_cadastrada = '1234'

if usuario == 'admin':
    print('Usuário correto!')
    senha = input('Digite sua senha: ')
    if senha == '1234':
        print('Você terá acesso total!')
    else:
        print(f'A senha {senha} está incorreta')
else:
    print('Usuário incorreto')