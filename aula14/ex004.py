''''

Ex. 4 - Crie um algoritmo com classe carro com marca, ano, cor e um método para mostrar as informações relacionadas a respectiva marca, ano e cor.

'''

class Carro():

    def __init__(self, marca, ano, cor):
        self.marca = marca
        self.ano = ano
        self.cor = cor

    def exibir_informacoes(self):
        print(f'A marca desse carro é da {self.marca} do ano {self.ano} na cor {self.cor}')

# Criando os carros

carro1 = Carro('Ferrari', '2009', 'Vermelha')
carro2 = Carro('Lamborghini', '2018', 'Roxa')

carro1.exibir_informacoes()
carro2.exibir_informacoes()