'''

Crie um algoritmo para verificar se o número é par ou ímpar, porém, crie variáveis para as condições.

'''

numero = int(input('Digite o número: '))

resto = numero % 2
eh_par = resto == 0
eh_impar = resto != 0

if eh_par:
    print('O número é par')
else:
    print('O número é ímpar')