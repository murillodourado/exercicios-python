# Ex.3 (exibir uma lista com nomes, cpf e uma lista aninhada com nome e cpf já formatado)

lista_nome = []
lista_cpf = []
lista_completa = []

for i in range(3):
    nome = input('Digite seu nome: ')
    cpf = input('Digite seu cpf: ')

    cpf_formatado = cpf[0:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:11]
    
    lista_nome.append(nome)
    lista_cpf.append(cpf_formatado)
    inserir_dados = [nome, cpf_formatado]

    lista_completa.append(inserir_dados)

print(f'Lista de nomes: {lista_nome}')
print(f'Lista de CPF: {lista_cpf}')
print(f'Lista completa: {lista_completa}')

