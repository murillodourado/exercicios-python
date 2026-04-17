lista_completa = []

while True:
    num = int(input('Digite um número: '))
    cpf = input('Digite seu CPF: ')

    if num == 0 or cpf == 0:
        break

    num_cpf = [num, cpf]
    lista_completa.append(num_cpf)
    print(lista_completa)