'''
5. Sistema de desconto. solicite valor e se a pessoa é vip ou não. Se valor maior ou igual 200,
crie estrutura de condição aninhada para verificar se a pessoa é vip, se for, 
ofereça 20% de desconto sobre o valor e mostre o valor a ser descontado e o valor final, considerando o desconto. 
Se não for vip, ofereça o desconto de 10%. 
'''

valor = float(input('Digite o valor: '))

if valor >= 200:
    vip = input('Você é vip? (sim/não): ').lower()
    if vip == 'sim':
        desconto = valor * 0.2
        valor_a_pagar = valor - desconto
        print(f'Você terá 20% de desconto, então o valor descontado será de {desconto} e o valor final será de {valor_a_pagar:.2f}')
    else:
        desconto = valor * 0.1
        valor_a_pagar = valor * 0.1
        print(f'Você terá 10% de desconto, então o valor descontado será de {desconto} e o valor final será de {valor_a_pagar:.2f}')
else:
    print('Você não terá desconto na compra.')