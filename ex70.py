# Estatísticas em produtos

print('-'*28)
print('     LOJA SUPER BARATÂO')
print('-'*28)
s = 0
c = 0

menor = 0
cont = 0

barato = ' '

while True:
    nomep = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$ '))
    s += preco
    cont += 1

    if preco > 1000:
        c += 1
    if cont == 1:
        menor = preco
        barato = nomep
    elif preco < menor:
        menor = preco
        barato = nomep

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()
        print('-'*28)

    if continuar == 'N':
        print('→→→→→ FIM DO PROGRAMA ←←←←←')
        break

print(f'O total da compra foi de R${s:.2f}')
print(f'Temos {c} produto(s) custando mais de R$1,000.00')
print(f'O produto mais barato foi {barato}, de valor = R${menor:.2f}')