# Sequência de Fibonacci v1.0
print('-='*15)
print('    Sequência de Fibonacci')
print('-='*15)
n = int(input('Quantos termos você quer mostrar? '))

p = 0
s = 1

print('{} → {}'.format(p, s), end=' ')
cont = 3
while cont <= n:
    t = p + s
    print('→ {}'.format(t), end=' ')
    p = s
    s = t
    cont += 1
print('FIM')