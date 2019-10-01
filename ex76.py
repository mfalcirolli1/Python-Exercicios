# Lista de Preços com Tupla

print('-='*25)
print('                LISTAGEM DE PREÇOS')
print('-='*25)
merc = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
for c in range(0, len(merc)):
    if c % 2 == 0:
        print(f'{merc[c]:.<41}', end=' ')
    else:
        print(f'R${merc[c]:>6.2f}')


print('-='*25)
