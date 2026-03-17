'''Crie um programa que calcule os valores de x1 e x2 que satisfazem a equação abaixo:
2x² + 4x - 6 = 0

'''
import math

delta = (4 ** 2) - 4 * 2 * -6
raiz_de_delta = math.sqrt(delta)
x1 = (-4 + raiz_de_delta) /  (2 * 2)
x2 = (-4 - raiz_de_delta) / (2 * 2)

print(x1)
print(x2)