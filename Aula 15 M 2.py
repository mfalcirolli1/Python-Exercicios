# Interrompendo repetições While

n = 0
s = 0
c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1
print('Quantidade {} Soma {}'.format(c, s))
#OU
print(f'Quantidade {c} Soma {s}')

#--------------------------------------------

nome = 'José'
idade = 33
salario = 1000
print(f'O {nome:-^20} tem {idade} anos e ganha {salario:.2f}')
