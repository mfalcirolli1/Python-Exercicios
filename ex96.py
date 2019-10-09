# Função que calcula área

def mult(a, b):
    m = a * b
    print(f'A área de um terreno {a} x {b} é de {m} m². ')


print('-'*20)
print('Controle de Terrenos')
print('-'*20)

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
mult(l, c)

