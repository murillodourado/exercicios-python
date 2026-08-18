# Crie uma classe para solicitar nome, curso, faculdade e semestre. Depois, crie uma função para apresentar o nome da pessoa, c om o respectivo curso, faculdade e semestre. Faça o teste para duas pessoas e print cada uma.

class Estudante:
    def __init__(self, nome, curso, faculdade, semestre):
        self.nome = nome
        self.curso = curso
        self.faculdade = faculdade
        self.semestre = semestre

    def apresentar_estudante(self):
        return f'Meu nome é {self.nome}, estou estudando {self.curso} na {self.faculdade} e estou no {self.semestre}º semestre.'

aluno1 = Estudante('Murillo', 'Engenharia de Software', 'FIAP', '2')
aluno2 = Estudante('Fulana', 'Medicina', 'USP', '5')

print(aluno1.apresentar_estudante())
print(aluno2.apresentar_estudante())