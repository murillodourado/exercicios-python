# Verificar número ímpar: se o número não for par

numero = int(input('Digite um número: '))

if not numero % 2 == 0:
    print('Número ímpar')
else:
    print('Número par')