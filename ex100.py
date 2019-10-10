# Funções para sortear e somar

from random import randint
from time import sleep

list = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]

def sort():
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in list:
        print(f'{c}', end=' ')
        sleep(0.3)
    print('FIM!')

def soma():
    s = 0
    print(f'Soma dos valores pares da lista: {list}', end=' ')
    for c in list:
        if c % 2 == 0:
            s += c
    print(f'= {s}')

sort()
soma()