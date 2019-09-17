# Analisando Triângulo

print('\033[7;30mInforme o tamanho de 3 retas e descubra se é possível que elas formem um triângulo.\033[m')
a1 = float(input('Primeira reta: '))
a2 = float(input('Segunda reta: '))
a3 = float(input('Terceira reta: '))
if a1 + a2 > a3 and a1 + a3 > a2 and a3 + a2 > a1:
    print('\033[1;32mSIM!\033[m É possível formar um triãngulo.')
else:
    print('\033[1;31mNÃO!\033[m Não possível formar um triângulo.')

#OU
#if a1 < a2 + a3 and a2 < a1 + a3 and a3 < a1 + a2: