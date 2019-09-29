# GAME Par ou Ímpar
from random import randint

print('-='*15)
print('VAMOS JOGAS PAR OU ÍMPAR')
print('-='*15)
c = 0

while True:
    n = int(input('Digite um valor de 1 a 10: '))
    esc = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    pc = randint(1, 10)
    total = n + pc
    p = 'PAR'
    i = 'IMPAR'

    if total % 2 == 0:
        print('-='*23)
        print(f'Você jogou {n} e o computador {pc}. Total {total} - {p}')
        if p[0] == esc:
            print('VOCE VENCEU!')
            c += 1
        else:
            print('O COMPUTADOR VENCEU!')
            print(f'GAME OVER!')
            break

    elif total % 2 == 1:
        print('-='*23)
        print(f'Você jogou {n} e o computador {pc}. Total {total} - {i}')
        if i[0] == esc:
            print('VOCÊ VENCEU!')
            c += 1
        else:
            print('O COMPUTADOR VENCEU!')
            print(f'GAME OVER!')
            break

    print('Vamos jogar novamente!')
print(f'{c} vitória(s).')
print('-='*23)


