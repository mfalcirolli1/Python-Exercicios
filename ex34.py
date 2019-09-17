# Aumentos múltiplos
import math
sal = float(input('Qual é o salário do funcionário: '))
reajuste1 = math.ceil(sal * 1.15)
reajuste2 = math.ceil(sal * 1.10)

if sal <= 1250:
    print('Quem ganha R${:.2f} terá reajuste salarial de 15%. E passará a receber R${:.2f}.'.format(sal, reajuste1))
else:
    print('Quem ganha R${:.2f} terá reajuste salarial de 10%. E passará a receber R${:.2f}.'.format(sal, reajuste2))

