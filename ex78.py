# Maior e Menor Valores na Lista

lista = []
for c in range(0, 5):
    lista.append(int(input('Digite um número: ')))
print('-='*28)
print(f'Valores digitados: {lista}')
print(f'O maior valor digitado foi {max(lista)}, na {lista.index(max(lista))+1}ª posição.')
print(f'O menor valor digitado foi {min(lista)}, na {lista.index(min(lista))+1}ª posição.')