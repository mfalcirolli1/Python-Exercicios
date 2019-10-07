# Cadastro de Jogador de Futebol

lista = {}
s = 0
lgol = []

lista['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {lista["nome"]} jogou? '))
for g in range(0, partidas):
    gols = int(input(f'   Quantos gols na {g+1}ª partida? '))
    lgol.append(gols)
    lista['gols'] = lgol
    s += gols
    lista['total'] = s

print('-='*25)
print(lista)
print('-='*25)
for k, v in lista.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*25)
print(f'O jogador {lista["nome"]} jogou {partidas} partidas, sendo que:')
for i, v in enumerate(lista["gols"]):
    print(f'=> Na partida {i+1}, fez {v} gol(s).')

