# Alistamento Militar

from datetime import date
ano = int(input('Ano de nascimento: '))
datual = date.today().year
idade = datual - ano
print('Você nasceu em {} e fez/fará {} anos em 2019.'.format(ano, idade))

if idade > 18:
    rest = idade - 18
    anoalist = datual - rest
    print('Você já deve ter se alistado há {} anos.'.format(rest))
    print('Seu alistamento foi em {}'.format(anoalist))

elif idade < 18:
    rest = 18 - idade
    anoalist = datual + rest
    print('Ainda faltam {} anos para o alistamento.'.format(rest))
    print('Seu alistamento será em {}.'.format(anoalist))
else:
    print('Aliste-se imediatamente!')