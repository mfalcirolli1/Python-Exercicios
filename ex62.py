# Progressão Aritmética v3.0  -  v2.0 ex61  -  v1.0 ex51

print('-='*16)
print('Gerador de Progressão Aritmética')
print('-='*16)
num = int(input('Primeiro termo: '))
rz = int(input('Razão: '))

c = 1
termo = num
total = 0
mais = 10

while mais != 0:
    total += mais
    while c <= total:
        print('{} ↔ '.format(termo), end=' ')
        c += 1
        termo += rz
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Processo finalizado com {} itens mostrados'.format(total))
print('FIM')