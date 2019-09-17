# Catetos e Hipotenusa
import math
n1 = float(input('Digite o valor do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(n1, n2)
print('A hipotenusa é igual a {:.2f}'.format(hip))

from math import hypot
n1 = float(input('Digite o valor do cateto oposto: '))
n2 = float(input('Digite o valor do cateto adjacente: '))
hip = hypot(n1, n2)
print('A hipotenusa é igual a {:.2f}'.format(hip))