# Calcular a área e perímetro de um retângulo a partir da base e altura. Crie a class com dois métodos(área e perímetro)


base = float(input('Digite o valor da base: '))
altura = float(input('Digite o valor da altura: '))

class Retangulo:
    
    def __init__(self, area, perimetro):
        self.area = area
        self.perimetro = perimetro

    def area():
        area_retangulo = base * altura
        return f'O valor da área desse retângulo é {area_retangulo:.2f}'

    def perimetro():
        perimetro_retangulo = (base * 2) + (altura * 2)
        return f'O valor do perímetro desse retângulo é {perimetro_retangulo:.2f}'

area_ret1 = (Retangulo.area())
per_ret1 = (Retangulo.perimetro())

print(area_ret1)
print(per_ret1)