# Cadastro de Trabalhador em Python
from datetime import date, datetime

trab = {}
datual = date.today().year

while True:
    trab['nome'] = str(input('Nome: '))

    ano = int(input('Ano de Nascimento: '))
    idade = datual - ano
    trab['idade'] = idade

    trab['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
    if trab['ctps'] == 0:
        break
    else:
        trab['contratacao'] = int(input('Ano de Contratação: '))
        trab['salario'] = int(input('Salário: '))
        aposentadoria = trab['idade'] + ((trab['contratacao'] + 35) - datual)
        trab['aposentadoria'] = aposentadoria

    print('-='*25)
    for k, v in trab.items():
        print(f'- {k} = {v}')

    break