'''

Verificar se a pessoa é adulta ou não em função da idade, porém, crie variáveis para as condições

'''

idade = int(input('Digite sua idade: '))

adulta = idade >= 18
nao_adulta = idade < 18

if adulta == True:
    print('Você é adulto')
else:
    print('Você não é adulto')