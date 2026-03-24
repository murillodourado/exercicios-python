'''
2. Classificação de idade. solicite idade, se idade for maior ou igual a 18, 
crie uma estrutura de condição aninhada para verificar se idade é maior ou igual a 60,
se for, mostre que é idoso, senão, mostre que é adulto. Se idade for maior ou igual a 12, adolescente, caso contrário, criança. 
'''

idade = int(input('Digite sua idade: '))

if idade >= 18:
    if idade >= 60:
        print('Idoso')
    else:
        print('Adulto')

else:
    if idade >= 12:
        print('Adolescente!')
    else:
        print('Criança!')