# Conversor de Moedas
n = float(input('Quanto de dinheiro você tem? (Utilize ponto para a casa decimal) R$ '))
dolar = n / 4.10
euro = n / 4.76
print('Com R${:.2f} você pode comprar US${:.2f} (Dólares)'.format(n, dolar), end='. ')
print('E E${:.2f} (Euros)'.format(euro))
