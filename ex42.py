# Analisando Triângulos v2.0

t1 = float(input('Primeiro segmento: '))
t2 = float(input('Segundo segmento: '))
t3 = float(input('Terceiro segmento: '))

if t1 + t2 > t3 and t1 + t3 > t2 and t3 + t2 > t1:
    if t1 == t2 == t3:
        print('Os segmento acima PODEM FORMAR um triângulo EQUILÁTERO.')
    elif t1 == t2 or t1 == t3 or t2 == t3:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES.')
    elif t1 != t2 != t3:
        print('Os segmentos PODEM FORMAR um triângulo ESCALENO.')
else:
    print('Não é possível formar um triângulo.')
