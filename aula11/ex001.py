# Estrutura de repetição com while

# Ex.1

entrada = int(input('Digite um número: '))
soma = 0

while entrada > 0:
    soma += entrada
    print(soma)
    entrada = int(input('Digite um número: '))