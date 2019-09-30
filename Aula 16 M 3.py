# Variáveis Compostas (Tuplas)
# Tuplas são imutáveis

pessoa = ('Matheus', 23, 'M')
del(pessoa)

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

for c in lanche:
    print(f'Eu vou comer {c}.')

for pos, c in enumerate(lanche):
    print(f'Eu vou comer {c} na ordem {pos}.')

for c in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[c]} na ordem {c+1}.')

print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(sorted(c))
print(len(c))
print(c.count(8))
print(c.index(2))

