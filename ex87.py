# Mais sobre Matriz em Python

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = 0
tcoluna = 0
maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l}, {c}]: '))
print('-='*16)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            s += matriz[l][c]
    print()

for l in range(0, 3):
    tcoluna += matriz[l][2]

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print('-='*16)
print(f'A soma dos valores pares é {s}.')
print(f'A soma dos valores da terceira coluna é {tcoluna}.')
print(f'O maior valor da segunda linha é {maior}.')