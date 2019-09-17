# Custo da viagem
from time import sleep
dist = float(input('Qual é a distância da sua viagem? (KM): '))
p1 = dist * 0.5
p2 = dist * 0.45
print('\033[1;32mCalculando...\033[m')
sleep(1)
if dist <= 200:
    print('O preço da sua passagem será de \033[1;31mR${:.2f}\033[m'.format(p1))
else:
    print('O preço da sua passagem será de \033[1;31mR${:.2f}\033[m'.format(p2))