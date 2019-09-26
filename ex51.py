# Progressão Aritmética
print('='*38)
print('10 TERMOS DE UMA PROGRESSÃO ARITMÉTICA')
print('='*38)

num = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
decimo = num + (10 - 1) * rz

for c in range(num, decimo + rz, rz):
    print(c, end=' ')
print('Acabou.')
