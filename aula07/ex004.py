''''
4. Verificação de número. Solicite número e verifique se é maior do que zero, 
se for, crie uma estrutura de condição aninhada para verificar se este número é par, se for, 
print positivo e par. Se não for, Positivo e ímpar. Se número for igual a zero, print zero, caso contrário negativo. 
'''

numero = int(input('Digite um número inteiro: '))

if numero > 0:
    if numero % 2 == 0:
        print('Número par e positivo')
    else:
        print('Numero ímpar e positivo')
else:
    if numero == 0:
        print('Zero')
    else:
        print('Negativo')