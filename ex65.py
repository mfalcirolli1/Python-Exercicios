# Maior e Menor Valores

s = 0
n = 0
c = 0
maior = 0
menor = 0
media = 0
continuar = 0

while continuar != 'N':

    n = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar? [S/N] ')).upper()

    if continuar not in 'NS':
        print('Opção inválida. Tente novamente.')

    c += 1
    s += n
    media = s / c

    if c == 1:
        maior = n
        menor = n
    elif n < menor:
        menor = n
    elif n > maior:
        maior = n
print('Você digitou {} números e a média foi {}.'.format(c, media))
print('O maior valor foi {} e o menor {}'.format(maior, menor))
