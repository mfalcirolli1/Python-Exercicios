# Aluguel de Carros
da = int(input('Quantos dias alugados? '))
kmr = float(input('Quantos KM rodados? '))
pap = ((da * 60) + (kmr * 0.15))
print('O total a pagar é de R${:.2f}.'.format(pap))
