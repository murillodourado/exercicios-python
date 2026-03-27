'''

Crie um algoritmo para mostrar o desconto e o salário a ser recebido em função das seguintes condições:

10%: para rendimentos de até 11.600 dólares.
12%: para rendimentos entre 11.600 e 47.150 dólares.
22%: para rendimentos entre 47.150 e 100.525 dólares.
24%: para rendimentos entre 100.525 e 191.950 dólares.
32%: para rendimentos entre 191.950 e 243.725 dólares.
35%: para rendimentos entre 243.726 e 609.350 dólares.
37%: para rendimentos superiores a 609.350 dólares.

'''

salario = float(input('Digite seu salário em DÓLAR: '))

desconto = 0
salario_atual = 0

desconto_10 = salario <= 11.600
desconto_12 = 11.600 <= salario <= 47.150
desconto_22 = 47.150 <= salario <= 100.525
desconto_24 = 100.525 <= salario <= 191.950
desconto_32 = 191.950 <= salario <= 243.725
desconto_35 = 243.725 <= salario <= 609.350
desconto_37 = salario >= 609.350

if desconto_10 == True:
    desconto = salario * 0.1
    print(f'O desconto a ser recebido será de ${desconto:.2f}')
    salario_atual = salario - desconto
    print(f'O seu salário atual será de ${salario_atual:.2f}')
elif desconto_12 == True:
    desconto = salario * 0.12
    print(f'O desconto a ser recebido será de ${desconto:.2f}')
    salario_atual = salario - desconto
    print(f'O seu salário atual será de ${salario_atual:.2f}')
elif desconto_22 == True:
    desconto = salario * 0.22
    print(f'O desconto a ser recebido será de ${desconto:.2f}')
    salario_atual = salario - desconto
    print(f'O seu salário atual será de ${salario_atual:.2f}')
elif desconto_24 == True:
    desconto = salario * 0.24
    print(f'O desconto a ser recebido será de ${desconto:.2f}')
    salario_atual = salario - desconto
    print(f'O seu salário atual será de ${salario_atual:.2f}')
elif desconto_32 == True:
    desconto = salario * 0.32
    print(f'O desconto a ser recebido será de ${desconto:.2f}')
    salario_atual = salario - desconto
    print(f'O seu salário atual será de ${salario_atual:.2f}')
elif desconto_35 == True:
    desconto = salario * 0.35
    print(f'O desconto a ser recebido será de ${desconto:.2f}')
    salario_atual = salario - desconto
    print(f'O seu salário atual será de ${salario_atual:.2f}')
else:
    desconto = salario * 0.37
    print(f'O desconto a ser recebido será de ${desconto:.2f}')
    salario_atual = salario - desconto
    print(f'O seu salário atual será de ${salario_atual:.2f}')