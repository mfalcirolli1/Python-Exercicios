# Tratando vários valores v1.0

s = 0
n = 0
c = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    s += n
    c += 1
    if n == 999:
        c -= 1
        s -= 999
print('Soma dos {} valores digitados = {}'.format(c, s))



#    s = 0
#   for c in range(1, 11):
#      n = int(input('Digite um número [999 para parar]: '))
#        s += n
#    print(s)