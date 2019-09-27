# Estrutura de repetição While
'''for c in range(1, 10):
    print(c, end=' ')
print('FIM')'''

c = 1
while c < 10:
    print(c, end=' ')
    c += 1
print('FIM')

#####################################################

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? S/N ')).upper()
print('FIM')

#####################################################

num = 1
par = 0
impar = 0
print('Digite 0 para finalizar.')
while num != 0:
    num = int(input('Digite um valor: '))
    if num != 0:
        if num % 2 == 0:
            par += 1
        elif num % 2 == 1:
            impar += 1
print('Números pares = {} e Número ímpares = {}'.format(par, impar))
print('FIM')
