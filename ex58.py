# Jogo da Adivinhação v2.0  -  v1.0 ex28

from random import randint

print('Sou seu computador...')
print('Acabei de de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual é?')

p = 0
c = 0
esc = randint(0, 10)
while esc != p:
    p = int(input('Qual é o seu palpite? '))
    if p < esc:
        print('Mais... Tente novamente.')
        c += 1
    elif p > esc:
        print('Menos... Tente novamente.')
        c += 1
    elif p == esc:
        print('Acertou! Com {} tentativas.'.format(c+1))
