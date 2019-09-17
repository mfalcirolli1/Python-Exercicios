# Radar eletrônico
from time import sleep

vel = int(input('Qual é a velocidade atual do seu carro: '))
multa = (vel - 80)
print('Downloading...')
sleep(2)

if vel > 80:
    print('MULTADO! Você excedeu o limite de velocidade que é de 80km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa * 7))
print('Tenha um bom dia! Dirija com segurança.')