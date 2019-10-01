# Análise de dados em uma Tupla

print('Digite 4 números.')
num = (int(input('Digite um número: '))),  (int(input('Digite um número: '))), (int(input('Digite um número: '))), (int(input('Digite um número: ')))

print(f'Você digitou os números: {num}')

print(f'O número 9 apareceu {num.count(9)} veze(s).')

if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print('Número 3 não encontrado.')

for c in num:
    if c % 2 == 0:
        print(f'Número par presente: {c}')
