'''

Crie um algoritmo com try/except para calcular a área do círculo e retângulo, peça para o usuário selecionar a figura geométrica, em função da escolha da figura, solicite os inputs. Traga ainda possível erro usando ValueError.

'''

def escolher_figura():
    escolha = input('''
    Qual figura geométrica você deseja calcular a área?
    1 (Retângulo)
    2 (Círculo)
    : ''')
    
    if escolha == '1':
        print('CALCULAR ÁREA DO RETÂNGULO')
        try:
            base = float(input('Digite o valor da base (cm): '))
            altura = float(input('Digite o valor da altura (cm): '))
            area = base * altura
            print(f'O valor da área desse retângulo é {area:.2f}cm')
        except ValueError:
            print('Valor não numérico!')
        print('------------------------------------')
    elif escolha == '2':
        print('CALCULAR ÁREA DO CÍRCULO')
        pi = 3.14
        try:
            raio = float(input('Digite o valor do raio (cm): '))
            area = pi * raio ** 2
            print(f'O valor da área desse círculo é {area:.2f}cm')
        except ValueError:
            print('Valor não numérico!')
        print('------------------------------------')
    else:
        print('Você não escolheu nenhuma opção válida!')

escolher_figura()