# Jogos de Dados em Python
from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
ranking = []

jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)

print('Valores sorteados')
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.65)
print('-='*15)

print('== RANKING DOS JOGADORES ==')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')