'''Solicite para o usuário um salário e retorne o respectivo desconto e valor a ser recebido em função da tabela de descontos do Brasil. 

Faixa Salarial (R$) 	                Alíquota	
Até 1.621,00		                    7,5%
De 1.621,01 até 2.902,84	            9%	
De 2.902,85 até 4.354,27	            12%	
De 4.354,28 até 8.475,55  	            14%	

'''

salario = float(input('Digite o seu salário: '))
primeira_aliquota = salario * 0.075
segunda_aliquota = salario * 0.09
terceira_aliquota = salario * 0.12
quarta_aliquota = salario * 0.14    

if salario <= 1621:
    print(f'A alíquota que você terá que pagar é de 7,5%. Portanto, o seu desconto é de R${primeira_aliquota:.2f} e seu salário será de R${salario - primeira_aliquota:.2f}')
elif salario > 1621.01 and salario < 2902.84:
    print(f'A alíquota que você terá que pagar é de 9%. Portanto, o seu desconto é de R${segunda_aliquota:.2f} e seu salário será de R${salario - segunda_aliquota:.2f}')
elif salario > 2902.85 and salario < 4354.27:
    print(f'A alíquota que você terá que pagar é de 12%. Portanto, o seu desconto é de R${terceira_aliquota:.2f} e seu salário será de R${salario - terceira_aliquota:.2f}')
else:
    print(f'A alíquota que você terá que pagar é de 14%. Portanto, o seu desconto é de R${quarta_aliquota:.2f} e seu salário será de R${salario - quarta_aliquota:.2f}')