'''
Ex.7 - Crie um algoritmo para solicitar a escolha do menu do café da manhã. 
1. Eggs. 
2. Pancakes 
3. Wafles 
4. Frutas 
Se for eggs, pergunte qual o tipo de acompanhamento. Se for frutas, pergunte qual o tipo de fruta e acompanhamento. 
Para cada caso, traga uma informação com print para o usuário  
'''

print('Escolha uma opção de café da manhã\nEggs\nPancakes\nWafles\nFrutas\n')

escolha_do_cafe = input('Digite sua escolha: ').lower()

if escolha_do_cafe == 'eggs':
    acompanhamento_eggs = input('Qual o tipo de acompanhamento?: ')
    print(f'Com o menu do café escolhido como {escolha_do_cafe}, seu café terá um acompanhemento de {acompanhamento_eggs}')
elif escolha_do_cafe == 'pancakes':
    print('O menu Pancakes não possui acompanhamentos. Portanto sua refeição será apenas de panquecas!')
elif escolha_do_cafe == 'wafles':
    print('O menu Wafles não possui acompanhamentos. Portanto sua refeição será apenas de wafles!')
elif escolha_do_cafe == 'frutas':
    tipo_fruta = input('Qual o tipo de fruta?: ')
    acompanhamento_fruta = input('Qual o acompanhamento da sua fruta?: ')
    print(f'Com o menu do café escolhido como {escolha_do_cafe}, você comerá um(a) {tipo_fruta} acompanhado de {acompanhamento_fruta}')