# Valores únicos em uma Lista

lista = []

while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Número duplicado. Não foi adicionado.')

    perg = str(input('Deseja continuar? [S/N] ')).upper()
    if perg == 'N':
        break
print('-='*30)
lista.sort()
print(f'Você digitou os números {lista}')
