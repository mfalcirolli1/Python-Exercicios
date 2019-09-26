# Soma dos pares

s = 0
cont = 0
for c in range(1, 7):
    num = int(input('Número {}: '.format(c)))

    if num % 2 == 0:
        s += num
        cont += 1
print('A soma entre os {} números pares presentes é igual a {}'.format(cont, s))
