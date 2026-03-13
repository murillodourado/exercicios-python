# Crie um algoritmo para solicitar a idade da pessoa e determine se ela é criança, adolescente, adulto jovem, meia idade ou idoso.

idade = int(input('Digite sua idade: '))

if idade <= 11:
    print('Você é uma criança.')
elif idade > 11 and idade < 18:
    print('Você é um adolescente.')
elif idade > 18 and idade < 40:
    print('Você é um jovem adulto.')
elif idade > 40 and idade < 60:
    print('Você é da meia idade.')
else:
    print('Você é um idoso.')               