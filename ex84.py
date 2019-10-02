# Lista composta e análise de dados

dado = []
pessoas = []
mai = men = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))

    if len(pessoas) == 0:
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]

    pessoas.append(dado[:])
    dado.clear()

    perg = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if perg in 'Nn':
        break

print('-='*25)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi {mai}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == mai:
        print(p[0], end='')
print(f'O menor peso foi {men}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == men:
        print(p[0], end='')