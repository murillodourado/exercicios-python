'''Sistema de desconto: inserir valor e se é vip ou não, se valor >= 200, desconto de 0.20, caso contrário, desconto de 0.10.
Se valor for menor do 200, não terá desconto.
'''

valor = float(input('Digite o valor: '))
vip = input('Você é vip? (sim/não): ')
vip_verificado = vip.lower()

if vip == 'sim' and valor >= 200:
    print(f'Você tem um desconto de 20%, portanto seu valor em cima do desconto será de {valor - (valor * 0.2)}')
elif vip == 'sim' and valor < 200:
    print(f'Você tem um desconto de 10%, portanto seu valor em cima do desconto será de {valor - (valor * 0.1)}')
else:
    print('Você não tem desconto por que não é vip')