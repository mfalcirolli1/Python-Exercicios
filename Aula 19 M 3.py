# Dicionários

pessoas = {'nome': 'Matheus', 'sexo': 'M', 'Idade': 22}
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

#del pessoas['sexo']
pessoas['nome'] = 'Joice'
pessoas['sexo'] = 'F'
pessoas['CEP'] = '07244-390'

for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[1]['sigla'])

estadoo = {}
brasill = []
for c in range(0, 3):
    estadoo['uf'] = str(input('Unidade Federativa: '))
    estadoo['sigla'] = str(input('Sigla do Estado: '))
    brasill.append(estadoo.copy())
for e in brasill:
    for k, v in e.items():
        print(f'{k} {v}')










