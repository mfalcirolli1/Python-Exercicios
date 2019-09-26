# GAME: Pedra Papel e Tesoura

from time import sleep
import random

print('Suas opções:'
'\n[0] PEDRA'
'\n[1] PAPEL'
'\n[2] TESOURA')

op = int(input('Qual é a sua jogada? '))

print('JO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PO!!!')
sleep(0.7)

print('-='*15)

lista = [0, 1, 2]
choice = random.choice(lista)

if choice == 0:
    print('Computador escolheu PEDRA.')
elif choice == 1:
    print('Computador escolheu PAPEL.')
elif choice == 2:
    print('Computador escolheu TESOURA.')

if op == 0:
    print('Jogador escolheu PEDRA.')
elif op == 1:
    print('Jogador escolheu PAPEL.')
elif op == 2:
    print('Jogador escolheu TESOURA.')
else:
    print('Opção inválida. Tente novamente.')

print('-='*15)

if op == choice:
    print('Empate! Joguem novamente!')
elif choice == 0 and op == 1:
    print('JOGADOR VENCE!')
elif choice == 0 and op == 2:
    print('COMPUTADOR VENCE!')
elif choice == 1 and op == 0:
    print('COMPUTADOR VENCE!')
elif choice == 2 and op == 0:
    print('JOGADOR VENCE!')
elif choice == 1 and op == 2:
    print('JOGADOR VENCE!')
elif choice == 2 and op == 1:
    print('COMPUTADOR VENCE!')

