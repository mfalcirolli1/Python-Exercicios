# Extraindo dados de uma Lista

lista = []

while True:
    lista.append(int(input('Digite um número: ')))

    perg = str(input('Deseja continuar? [S/N] ')).upper()
    if perg not in 'Ss':
        break

lista.sort(reverse=True)
print('-='*30)
print(f'Você digitou {len(lista)} elementos.')
print(f'Ordem decrescente da lista = {lista}')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
