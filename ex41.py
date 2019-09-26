# Classificando Atletas

from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM.')
elif 10 <= idade <= 14:
    print('Classificação: INFANTIL.')
elif 15 <= idade <= 19:
    print('Classificação: JÚNIOR.')
elif 20 <= idade <= 25:
    print('Classificação: SÊNIOR.')
else:
    print('Classificação: MASTER.')
