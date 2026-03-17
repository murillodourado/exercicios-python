'''Calcular o ângulo de um triângulo retângulo, sabendo que o cateto oposto = 5 e hipotenusa = 10.

sin(x) = cateto oposto / hipotenusa
arcsen x = ângulo
'''

import math

cateto_oposto = 5
hipotenusa = 10 

angulo = math.asin((cateto_oposto / hipotenusa))

print(f'O ângulo é {angulo}°')