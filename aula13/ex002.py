try:
    a = int(input('Digite um número: '))
    b = int(input('Digite um número: '))
    resultado = a / b
    print(resultado)
except ZeroDivisionError:
    print('Divisão por zero não é permitida')
except ValueError:
    print('Você não digitou um número!')