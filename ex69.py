# Análise de dados de grupo
maior = 0
sex = 0
mulher = 0

while True:
    print('-'*25)
    print('   CADASTRE UMA PESSOA')
    print('-'*25)
    sexo = ' '
    
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()

    if idade >= 18:
        maior += 1
    if sexo in 'Mm':
        sex += 1
    if sexo == 'F':
        if idade < 20:
            mulher += 1

    print('-'*25)
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()
    print('-'*25)

    if continuar == 'N':
        break

print(f'Total de pessoas com idade maior ou igual a 18 anos: {maior}')
print(f'Ao todo temos {sex} homem(ns) cadastrados.')
print(f'E temos {mulher} mulher(es) com menos de 20 anos.')