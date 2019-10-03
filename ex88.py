# Palpites para a Mega Sena

from random import randint
from time import sleep
print('-'*39)
print('               MEGA SENA')
print('-'*39)

perg = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*5, f'SORTEANDO {perg} JOGOS', '-='*5)

lista = []
n = 0
for c in range(1, perg+1):
    numeros = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    numeros.sort()
    print(f'Jogo {c}: {numeros}')
    sleep(0.75)
print('-='*6, '<BOA SORTE !>', '-='*6)


