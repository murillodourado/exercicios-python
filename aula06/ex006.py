'''Aprovação com destinção: se nota >= 6, mas o aluno conseguiu acima de 9, aprovado com excelência, else aprovado, abaixo de 6, reprovado
'''

nota = float(input('Digite sua nota: '))

if nota >= 9:
    print('Aprovado com excelência')
elif nota >= 6 and nota < 9:
    print('Aprovado')
else:
    print('Reprovado')