class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f'Olá, eu sou {self.nome} e tenho {self.idade} anos.'

# Criando objeto

p1 = Pessoa('Murillo', 18)
p2 = Pessoa('Renan', 18)
print(p1.apresentar())