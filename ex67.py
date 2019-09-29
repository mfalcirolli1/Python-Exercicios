# Tabuada v3.0

n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*35)

    if n < 0:
        break

    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')

print('Programa encerrado. Volte sempre!')
