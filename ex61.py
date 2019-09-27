# Progressão Aritmética v2.0  -  v1.0 ex51

print('\033[1;7m-=\033[m'*16)
print('Gerador de Progressão Aritmética')
print('\033[1;7m-=\033[m'*16)

num = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
termo = num
c = 1
while c <= 10:
    print('{} ↔ '.format(termo), end='')
    termo += rz
    c += 1
print('FIM')
