# Sabendo que a equação de Energia é E = mxC**2, calcule o valor de E, tendo em vista que o usuário poderá inserir o valor de m

massa = float(input('Digite o valor da massa (kg): '))
velocidade_luz = 3*10**8

energia = massa * velocidade_luz ** 2
print(f'O valor de energia(joules) é : {energia}')
