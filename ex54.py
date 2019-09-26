# Grupo de Maioridade

from datetime import date
anoatual = date.today().year

cmaior = 0
cmenor = 0

for c in range(1, 8, 1):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = anoatual - ano

    if idade >= 18:
        cmaior += 1
    elif idade < 18:
        cmenor += 1
        
print('Ao todo tivemos {} pessoas maiores de idade.'.format(cmaior))
print('E também tivemos {} pessoas menores de idade.'.format(cmenor))