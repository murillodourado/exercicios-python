'''
Classificação de temperatura: solicitar temperatura para o usuário.

Muito frio se temperatura <= 10
agradável se temperatura for entre 26 e 35
muito quente se temperatura > 35
'''

temperatura = float(input('Digite a temperatura atual: '))

if temperatura <= 10:
    print('Muito frio')
elif temperatura >= 11 and temperatura <= 35:
    print('Clima agradável')
else: 
    print('Muito quente')