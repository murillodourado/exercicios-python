#
potencia = float(input('Digite o valor da potência: '))
tensao = float(input('Digite o valor da voltagem: '))

resistencia = (tensao ** 2) / potencia

print(f'O respectivo valor da resistência é: {resistencia:.2f}')