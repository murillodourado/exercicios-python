# Crie um algoritmo para solicitar o salário recebido durante o mês e calcule o imposto a ser pago, bem como o salário a ser recebido.

salario = float(input('Digite o salário que recebe: '))
imposto = salario * 0.15
imposto_a_ser_pago = imposto

print(f'Se o seu salário é de R${salario}, você terá que pagar R${imposto_a_ser_pago:.0f} de imposto. Portanto, seu salário será de R${salario - imposto_a_ser_pago:.2f}') 
