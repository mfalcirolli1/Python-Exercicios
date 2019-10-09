# Função que descobre o maior

from time import sleep

def linha():
    print('-='*30)


def maior(*num):
    maior = cont = 0
    print('Analisando os valores passados...')
    for c in num:
        print(f'{c}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        cont += 1
    print()
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado é {maior}.')
    linha()

maior(4, 7, 8)
maior(4, 1, 2, 1, 9)