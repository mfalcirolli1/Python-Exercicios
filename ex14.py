# Conversor de Temperaturas
c = float(input('Informe quantos °C deseja converter para °F e K: '))
f = (c * (9/5)) + 32
k = c + 273.15
print('A temperatura de {:.2f} °C corresponde a {:.2f} °F'.format(c, f), end=', ')
print('e a {:.2f} K.'.format(k))
