'''Login com bloqueio. solicitar senha e tentativas. Sabendo que o usuário terá até 3 tentativas.
Solicitar a senha para ter acesso ao sistema. (sem usar estrutura de repetição)
'''

senha_correta = '1234'

# 1ª Tentativa
senha = input('Digite a senha: ')

if senha == senha_correta:
    print('Você entrou no sistema!')
else:
    print('Senha incorreta. Tentativa 2 de 3.')

    # 2ª Tentativa
    senha = input('Digite sua senha:')
    
    if senha == senha_correta:
        print('Você entrou no sistema!')
    else:
        print('Senha incorreta. Tentativa 3 de 3.')

        # 3ª Tentativa
        senha = input('Digite sua senha: ')

        if senha == senha_correta:
            print('Você entrou no sistema!')
        else:
            print('Senha incorreta. Você excedeu o número de tentativas, usuário bloqueado!')