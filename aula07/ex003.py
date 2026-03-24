'''
3. Aprovação com distinção. solicite nota, se nota for maior ou igual a 6, 
crie condição aninhada para verificar se nota é maior ou igual a 9, 
se for aprovado com excelência. Se nota não for maior ou igual a 9, Aprovado. Caso contrário, reprovado.
'''

nota = float(input('Digite sua nota: '))

if nota >= 6:
    if nota >= 9:
        print('Aprovado com excelência!')
    elif nota < 9:
        print('Aprovado')
else:
    print('Reprovado')