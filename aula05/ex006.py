salario = 3000

if salario >= 3000:
    desconto = 300 * (5 / 100)
    salario_receber = salario - desconto
    print(f'O desconto será {desconto} e o salário a receber será de {salario_receber}')
else:
    print('Não terá desconto no salário')