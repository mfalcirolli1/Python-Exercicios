# Boletim com listas compostas

from time import sleep

lista = []
alunos = []

while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = ((n1 + n2) / 2)
    lista.append([nome, [n1, n2], media])

    perg = str(input('Deseja continuar? [S/N} ')).upper()
    if perg not in 'Ss':
        break
print('-='*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('_'*25)
for i, a in enumerate(lista):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8}')

while True:
    print('-' * 60)
    opc = int(input('Mostrar notas de qual aluno? [Digite 999 para interromper.] '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
sleep(0.75)
print('Obrigado. Volte Sempre.')