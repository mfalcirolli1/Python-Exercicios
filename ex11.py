# Pintando Parede
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
a = larg * alt
lit = a / 2
print('Sua parede tem dimensão {}x{} e sua área é de {:.3f}m².'.format(larg, alt, a))
print('Para pintar sua parede, você vai precisar de {}L de tinta.'.format(lit))


