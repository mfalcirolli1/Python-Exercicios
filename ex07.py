# Média Aritmética
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
ma = (n1 + n2) / 2
print('A média entre as notas {} e {} é {}.'.format(n1, n2, ma))

# Outra maneira utilizando apenas 2 variáveis

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('A média entre as notas {:.1f} e {:.1f} é {:.1f}.'.format(n1, n2, ((n1 + n2)/2)))
