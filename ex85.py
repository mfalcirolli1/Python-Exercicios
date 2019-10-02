# Listas com pares e ímpares
lista = []
par = []
impar = []
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º número: '))
    if n % 2 == 0:
        lista.append(n)
        par.append(n)
    else:
        lista.append(n)
        impar.append(n)
print(f'Os valores pares digitados foram: {par}')
print(f'Os valores ímpares digitados foram: {impar}')
print('-=' * 35)