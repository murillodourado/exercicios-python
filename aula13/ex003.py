def entrada_numero():

    try:
        numero = int(input('Digite um número: '))
        print(f'O número digitado é {numero}')
    except ValueError:
        print('Você não digitou um número!')

entrada_numero()