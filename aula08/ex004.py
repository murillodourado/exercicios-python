''''

Crie um algoritmo para solicitar idade e se possui CNH. Porém, crie variáveis para as condições

'''

idade = int(input('Digite sua idade: '))

idade_permitida = idade >= 18

if idade_permitida:
    print('Você é maior de idade!')

    cnh = input('Você tem CNH? (Sim) ou (Não)?: ').lower()
    tem_cnh = cnh == 'sim'

    if tem_cnh == True:
        print('Você já possuí uma CNH, então não precisa emitir outra')
    else:
        print('Você não tem CNH, mas pode emitir uma já que é maior de idade')
else:
    print('Você não pode emitir uma CNH porque não é de maior')