# Analisador completo

s = 0
media = 0
maioridadeh = 0
nomevelho = 0
mulhermenos20 = 0

for c in range(1, 5):
    print('-----{}ª PESSOA -----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    s += idade

    if c == 1 and sexo == 'M':
        maioridadeh = idade
        nomevelho = nome
    if idade > maioridadeh and sexo == 'M':
        maioridadeh = idade
        nomevelho = nome

    if sexo == 'F' and idade < 20:
        mulhermenos20 += 1

media = s / 4
print('A média de idade do grupo é de {}'.format(media))
print('O homem mais velho é o {}, de {} anos.'.format(nomevelho, maioridadeh))
print('Existem {} mulheres menores de 20 anos.'.format(mulhermenos20))


