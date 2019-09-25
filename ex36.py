# Empréstimo bancário

from time import sleep
print('\033[7mDigite os dados a seguir para saber se você tem direito a um empréstimo bancário.\033[m')

vcasa = float(input('Qual é o valor da casa que deseja comprar? R$'))
sal = float(input('Qual é o seu salário? R$'))
i = int(input('Em quantos anos pretende pagar a casa? '))

prest = (vcasa / (i*12))
minimo = (sal * 0.3)
porcent = (prest / sal) * 100

print('\033[7mO valor da prestação mensal será de R${:.2f}. Caso a prestação exceda 30% do seu salário, o empréstimo será negado.\033[m'.format(prest))
print('Processando...')
sleep(4)
if prest > minimo:
    print('\033[7mEmpréstimo negado. O valor das parcelas chegou a {:.2f}% do seu salário\033[m'.format(porcent))
else:
    print('\033[7mEmpréstimo aprovado! O valor das parcelas chegou a {:.2f}% do seu salário'.format(porcent))