# Ficha do Jogador


def ficha(jog, gol):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


print('-=' * 20)
nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
if nome.strip() == '':
    nome = '<desconhecido>'
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

ficha(nome, gols)
