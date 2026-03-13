'''Solicite ao usuário 3 informações: corrente, resistência e tensão.

tensao = 0 e corrente = 0 - Não é possivel calcular a potência.
corrente = 0 e resistência = 0 - Não é possivel calcular a potência.
resistencia = 0 e tensão = 0 - Não é possivel calcular a potência.
tensão = 0 - corrente ** 2 * resistência
corrente = 0 - tensão ** 2 / resistência
resistência = 0 - tensão * corrente

'''

# else - valores de corrente, tensão e corrente não podem ser todos zero.

tensao = float(input('Digite o valor da tensão: '))
corrente = float(input('Digite o valor da corrente: '))
resistencia = float(input('Digite o valor da resistencia: '))

if tensao == 0 and corrente == 0:
    print('Não é possível calcular a potência')
elif corrente == 0 and resistencia == 0:
    print('Não é possível calcular a potência')
elif resistencia == 0 and tensao == 0:
    print('Não é possivel calcular a potência')
elif tensao == 0:
    valor_tensao = (corrente ** 2) * resistencia
    print(f'O valor da tensão é {valor_tensao}')
elif corrente == 0:
    valor_corrente = (tensao ** 2) / resistencia
    print(f'O valor da corrente é {valor_corrente}')
elif resistencia == 0:
    valor_resistencia = tensao * corrente
    print(f'O valor da resistência é {valor_resistencia}')