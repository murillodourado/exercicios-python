import pandas as pd

dados = {
    'produto': ['notebook', 'mouse', 'teclado', 'monitor', 'webcam'],
    'vendas': [1200, 300, 450, 800, None],
    'lucro': [300, 50, 80, 200, 40],
    'ano': ['2022', '2022', '2022', '2022', 'dois mil e vinte e dois']
}

dataframe = pd.DataFrame(dados)

try:
    media = dataframe['lucro'].mean()
    print(f'Média do estoque: {media}')
except KeyError:
    print('A coluna não existe no dataframe')