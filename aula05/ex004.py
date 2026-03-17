'''
Classificação de crédito

Aprovado - renda >= 300 e score <= 700
Análise manual - renda >= 2000 e score >= 600
Caso contrário - Negado
'''

renda = float(input('Digite sua renda: '))
score = float(input('Digite seu score: '))

if renda >= 300 and score <= 700:
    print('Aprovado')
elif renda >= 2000 and score >= 600:
    print('Análise manual')
else:
    print('Negado')