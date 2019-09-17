# Jogo da Adivinhação
import random
from time import sleep
print('Eu vou pensar em um número entre 0 e 5. Tente adivinhar qual eu vou escolher.')
lista = [0, 1, 2, 3, 4, 5]
esc = random.choice(lista)
n = int(input('Digite um número entre 0 e 5: '))
print('\033[1;36mPROCESSANDO...\033[m')
sleep(2)
if n == esc:
    print('Parabéns, você venceu! Eu também escolhi o número {}.'.format(esc))
else:
    print('Você perdeu! Eu escolhi o número {}.'.format(esc))

#OU

import random
from time import sleep
print('Eu vou pensar em um número entre 0 e 5. Tente adivinhar qual eu vou escolher.')
esc = random.randint(0, 5)
n = int(input('Digite um número entre 0 e 5: '))
print('PROCESSANDO...')
sleep(2)
if n == esc:
    print('Parabéns, você venceu! Eu também escolhi o número {}.'.format(esc))
else:
    print('Você perdeu! Eu escolhi o número {}.'.format(esc))