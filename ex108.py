# Formatando Moedas em Python

import uteis

valor = float(input('Digite o preço: R$'))

print(f'A metade de {uteis.moeda(valor)} é {uteis.moeda(uteis.metade(valor))}')
print(f'O dobro de {uteis.moeda(valor)} é {uteis.moeda(uteis.dobro(valor))}')
print(f'Aumentando 10%, temos {uteis.moeda(uteis.porcentagem(valor))}')