from math import sqrt

# Para a equação a^2 = b^2 + c^2. Calcule o valor de b, sabendo que o usuário poderá inserir os valor de a e c.

valor_a = int(input('Digite o valor de a: '))
valor_c = int(input('Digite o valor de c: '))
calculo_b = (valor_a ** 2) - (valor_c ** 2)
raiz = sqrt(calculo_b)

print(f'O valor de b é {raiz:.2f}')