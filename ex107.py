# Exercitando módulos em Python

import uteis

valor = float(input('Digite o preço: R$'))

print(f'A metade de R${valor:.2f} é R${uteis.metade(valor):.2f}')
print(f'O dobro de R${valor:.2f} é R${uteis.dobro(valor):.2f}')
print(f'Aumentando 10%, temos R${uteis.porcentagem(valor):.2f}')
