# Senha proibída (se a senha não for 123456)

senha = input('Digite uma senha: ')

if not senha == '123456':
    print('Senha inválida')
else:
    print('Senha válida')