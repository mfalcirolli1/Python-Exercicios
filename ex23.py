# Separando digitos de um número
num = int(input('Digite um número: '))
n = str(num)
uni = n[3]
dez = n[2]
cen = n[1]
mil = n[0]

print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cen))
print('Milhar: {}'.format(mil))

# OU
print('-' * 25)

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))