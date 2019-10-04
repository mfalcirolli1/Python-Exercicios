# Dicionário em Python

aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média do {aluno["nome"]}: '))
print('-='*25)

print(f' - nome é igual a {aluno["nome"]}')
print(f' - média é igual a {aluno["média"]}')

if aluno["média"] < 4:
    print(' - situação é igual a Reprovado.')
    aluno['situacao'] = 'Reprovado'

elif 4 < aluno["média"] < 7:
    print(' - situação é igual a Recuperação.')
    aluno['situacao'] = 'Recuperação'

elif aluno["média"] >= 7:
    print(' - situação é igual a Aprovado.')
    aluno['situacao'] = 'Aprovado'

print()
# Ou simplesmente:

for k, v in aluno.items():
    print(f' - {k} é igual a {v}.')
