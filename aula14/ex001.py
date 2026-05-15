# Ex. 1 - Uma Introdução básica a POO

class Pessoa():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Meu nome é {self.nome} e tenho {self.idade} anos.')

# Criar os objetos
p1 = Pessoa('julia', 29)
p2 = Pessoa('Murillo', 18)

p1.apresentar()
p2.apresentar()