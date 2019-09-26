# Soma ímpares múltiplos de três

s = 0
cont = 0

for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        print(c, end=' ')
        cont += 1
        s += c
print('\nA soma de todos os {} valores ímpares, múltiplos de três, de 1 a 500 é {}.'. format(cont, s))
