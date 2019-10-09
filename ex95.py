# Aprimorando os Dicionários
time = []
lista = {}
s = 0
lgol = []

while True:
    lista.clear()
    lista['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {lista["nome"]} jogou? '))
    lgol.clear()
    for g in range(0, partidas):
        lgol.append(int(input(f'   Quantos gols na {g+1}ª partida? ')))
    lista['gols'] = lgol[:]
    lista['total'] = sum(lgol)
    time.append(lista.copy())

    while True:
        perg = str(input('Deseja continuar [S/N]? ')).upper().strip()
        if perg in 'SN':
            break
        else:
            print('ERRO! Digite apenas "S" ou "N".')
    if perg == 'N':
        break

print('-='*25)

print('cod ', end='')
for i in lista.keys():
    print(f'{i:<15}', end='')
print()

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*25)

while True:
    busca  = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca > len(time):
        print('ERRO! Jogador inexistente.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f' No jogo {i+1} fez {g} gol(s).')
    print('-='*25)
print('Volte Sempre.')