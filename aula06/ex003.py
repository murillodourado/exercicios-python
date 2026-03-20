# Acesso negado por idade - se idade não for menor do que 18

idade = int(input('Digite sua idade: '))

if not idade < 18:
    print('Acesso liberado')
else:
    print('Acesso negado')