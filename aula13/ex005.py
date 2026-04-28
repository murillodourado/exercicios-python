'''

Solicitar ao usuário uma temperatura em celsius e converter em fahrenheit

fahrenheit = (celsius * 9/5) + 32

'''

def calcular_temperatura():
    try:
        temp_celsius = float(input('Digite a temperatura em °C: '))
        calc_fahreinheit = (temp_celsius * 9/5) + 32
        print(f'{temp_celsius}°C em fahreinheit é {calc_fahreinheit}')
    except ValueError:
        print('Você não digitou o valor correto!')

calcular_temperatura()