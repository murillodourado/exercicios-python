'''
6. Crie um algoritmo para perguntar para o usuário qual o dia da semana, caso seja sábado, escreva dia de festa. 
Caso seja, domingo, pergunte sobre a condição física do usuário, se estiver com dores de cabeça, 
print recuperando, então, precisa descansar. Caso contrário, apenas descanse. 
Caso não seja sábado ou domingo, mostre trabalhando, trabalhando e trabalhando! 
'''

dia_semana = input('Digite qual o dia da semana?: ').lower()

if dia_semana == 'sabado':
    print('Dia de festa!')
elif dia_semana == 'domingo':
    condicao_fisica = input('Você está com dores de cabeça? (sim/não): ').lower()
    if condicao_fisica == 'sim':
        print('Recuperando, então precisa descansar.')
    else:
        print('Apenas descanse.')
else:
    print('Trabalhando, trabalhando e trabalhando!')