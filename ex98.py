# Função de Contador

from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f}, de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}  ', end='')
            sleep(0.3)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}  ', end='')
            sleep(0.3)
            cont -= p
        print('FIM!')


print('-='*20)

print('Contagem de 1 até 10 de 1 em 1')
for c in range(1, 11):
    print(f'{c}  ', end='')
    sleep(0.3)
print('FIM!')

print('-='*20)

print('Contagem de 10 até 0 de 2 em 2')
for d in range(10, -1, -2):
    print(f'{d}  ', end='')
    sleep(0.3)
print('FIM!')

print('-='*20)

print('Agora é a sua vez de personalizar a contagem!')

ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))

print('-='*20)

contador(ini, fim, pas)

