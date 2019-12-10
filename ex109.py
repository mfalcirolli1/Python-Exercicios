# Formatando Moedas em Python v2.0

import uteis

valor = float(input('Digite o preço: R$'))

print(f'A metade de {uteis.moeda(valor)} é {uteis.metade(valor, True)}')
print(f'O dobro de {uteis.moeda(valor)} é {uteis.dobro(valor, True)}')
print(f'Aumentando 10%, temos {uteis.porcentagem(valor, True)}')
print(f'Reduzindo 10%, temos {uteis.porcentagemr(valor, True)}')