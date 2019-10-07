# Unindo Dicionários e Listas

sexo = ''
perg = ''
lista = []
dic = {}
soma = media = 0

while perg != 'N':
    dic.clear()
    dic['nome'] = str(input('Nome: '))

    while sexo != 'M' or 'F':
        dic['sexo'] = str(input('Sexo [M/F]: ')).upper()

        if sexo not in 'MF':
            print('ERRO! Digite apenas "M" ou "F"')
        elif sexo in 'MF':
            break

    dic['idade'] = int(input('Idade: '))
    lista.append(dic.copy())
    soma += dic['idade']

    perg = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if perg not in 'SN':
        print('ERRO! Digite apenas "S" ou "N"')
    elif perg == 'N':
        break

print('-='*25)
print(f'A) Ao todo temos {len(lista)} pessoa(s) cadastrada(s).')
media = soma / len(lista)
print(f'B) A média de idade é de {media:.2f} anos.')
print('C) As mulheres cadastradas são:')
for c in lista:
    if c['sexo'] == 'F':
        print(f'-→ {c["nome"]}')
print('D) Lista das pessoas que possuem idade acima da média:')
for a in lista:
    if a["idade"] > media:
        print(f'-→ {a["nome"]}, de {a["idade"]} anos.')
print('Finalizado.')