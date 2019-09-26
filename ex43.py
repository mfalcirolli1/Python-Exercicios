# Índice de Massa Corporal

print('Digite seus dados para descobrir qual é o seu Índice de Massa Corporal.')
p = float(input('Qual é o seu peso? (Kg) '))
a = float(input('Qual é a sua altura? (m) '))
imc = (p/a**2)
print('Seu IMC é de {:.2f}.'.format(imc))
if imc < 18.5:
    print('Abaixo do peso!')
elif 18.6 <= imc <= 24.9:
    print('Peso ideal!')
elif 25 <= imc <= 29.9:
    print('Levemente acima do peso!')
elif 30 <= imc <= 34.9:
    print('Obesidade grau 1!')
elif 35 <= imc <= 39.9:
    print('Obesidade grau 2 (severa)!')
elif imc >= 40:
    print('Obesidade grau 3 (mórbida)!')
