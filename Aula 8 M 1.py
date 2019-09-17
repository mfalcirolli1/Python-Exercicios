# Módulos
import math
n = int(input('Digite um número: '))
rq = math.sqrt(n)
print('A raíz de {} e igual a {:.2f}'.format(n, rq))

# from math import sqrt
# n = int(input('Digite um número: '))
# rq = sqrt(n)
# print('A raíz de {} e igual a {:.2f}'.format(n, rq))

import random
n1 = random.random()
print(n1)

n2 = random.randint(1, 10)
print(n2)

import emoji
print(emoji.emojize('Olá, Mundo! :earth_americas:', use_aliases=True))
print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
print(emoji.emojize(':camera: :computer: :cd: :telephone_receiver: :radio: :watch: :calling: :pray:', use_aliases=True))