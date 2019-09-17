# Quebrando um número
from math import trunc
n = float(input('Digite um número: '))
print('O valor digitado foi {:.3f} e a sua porção intera é {:.3f}.'.format(n, trunc(n)))

# Floor ou Trunc

n = float(input('Digite um número: '))
print('O valor digitado foi {:.3f} e a sua porção intera é {:.3f}.'.format(n, int(n)))

# Int