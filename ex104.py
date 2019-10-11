# Validando entrada de dados em Python


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


print('-=' * 35)
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
