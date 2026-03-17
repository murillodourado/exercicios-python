'''Se o salário for menor do que 2000 e o funcionáro morar mais de 30km do trabalho, retorne
Precisará de condução, caso contrário,
não precisará de condução.
'''

salario = float(input('Digite seu salário: '))
distancia_do_trabalho = float(input('Digite a distância da sua casa até o trabalho: '))

if salario <= 2000 and distancia_do_trabalho >= 30:
    print('Funcionário precisará de condução')
else:
    print('Funcionário não precisará de condução')

