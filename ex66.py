# Vários Números com Flag

n = 0
s = 0
c = 0
while True:
    n = int(input('Digite um número inteiro. (Digite 999 para finalizar): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Quantidade de números digitados = {c} | Soma dos números digitados = {s}')