''' Verificação de número: se > 0 e se numero for par, mostre que é positivo e par. Caso contrário, positivo e ímpar. Se = 0, mostrar que é zero,
caso contrário, número negativo
'''

numero = int(input('Digite um número inteiro: '))

if numero > 0 and numero % 2 == 0:
    print(f'{numero} é positivo e par!')
elif numero % 2 != 0:
    print(f'{numero} é positivo e ímpar!')
else:
    print(f'{numero} é um número negativo')