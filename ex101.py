# Funções para votação

from datetime import date


def voto(ano):
    anoatual = date.today().year
    idade = anoatual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade <= 17 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


print('-='*25)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
