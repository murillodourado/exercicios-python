# Escreva um programa que calcule o tempo de uma viagem de carro.

distancia = float(input('Digite a distância percorrida (km): '))
velocidade_media = int(input('Digite a velocidade média percorrida durante o trajeto (km/h): '))

tempo_da_viagem = distancia / velocidade_media

print(f'O tempo dessa viagem com uma distância de {distancia} e uma velocidade média de {velocidade_media} é {tempo_da_viagem}')