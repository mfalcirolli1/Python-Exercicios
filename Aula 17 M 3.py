# Listas (Parte 1)
# Listas são mutáveis

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.insert(2, 2)
print(num)
print(len(num))

num.pop(3)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)

valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))

for p, c in enumerate(valores):
    print(f'Valor {c} na {p+1}ª posição')


a = [2, 4, 5, 8]
b = a[:]
b[2] = 9
print(a)
print(b)







'''lanche = ['Pizza', 'Sorvete', 'HG']
lanche.append('Café')
lanche.insert(1, 'Suco')
print(lanche)

del lanche[3]
lanche.pop(0)
lanche.remove('Suco')
print(lanche)

valores = list(range(4, 11))
print(valores)

valores2 = [2, 4, 7, 10, 1, 60]
print(len(valores2))'''