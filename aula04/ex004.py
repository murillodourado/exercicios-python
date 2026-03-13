# Solicite um valor de temperatura em fahrenheit e transforme para Graus Celsius. C = (F - 32) / 1,8

valor_fahrenheit = float(input('Digite o valor da temperatura em fahrenheit que deseja transformar: '))
c = (valor_fahrenheit - 32) / 1.8

print(f'O valor da temperatura em Graus Celsius é: {c:.2f}')