# Ex 3

numeros = []
soma = 0

while True:
    num = int(input('Digite um número: '))

    if num == 0:
        break

    numeros.append(num)
    soma += num
    print(numeros)
    print(soma)

while numeros:
    atender = numeros.pop()
    print(atender)