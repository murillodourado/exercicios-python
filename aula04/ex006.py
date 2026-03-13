# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos

dias = float(input('Digite a quantidade de dias: '))
horas = float(input('Digite a quantidade de horas: '))
minutos = float(input('Digite a quantidade de minutos: '))
segundos = float(input('Digite a quantidade de segundos: '))
dia = dias * 24

calc = (dia * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

print(f'O total de segundos nessa linha de tempo é {calc:.0f} segundos')