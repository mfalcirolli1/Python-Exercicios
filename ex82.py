# Dividindo valores em várias Listas

lista = []
par = []
impar = []
while True:
    n = (int(input('Digite um número: ')))
    if n % 2 == 0:
        lista.append(n)
        par.append(n)
    else:
        lista.append(n)
        impar.append(n)

    perg = str(input('Quer continuar: [S/N] ')).upper()
    if perg in 'Nn':
        break

lista.sort()
print('-='*25)
print(f'A lista completa em ordem crescente é: {lista}')
print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')
