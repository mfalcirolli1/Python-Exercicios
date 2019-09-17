# Conversor de medidas
m = float(input('Distância em metros: '))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m * 0.1
hm = m * 0.01
km = m * 0.001

print('A medida de {:.1f}m corresponde a:'.format(m))
print('{}km\n{}hm\n{}dam\n{}dm\n{}cm\n{}mm'.format(km, hm, dam, dm, cm, mm))

