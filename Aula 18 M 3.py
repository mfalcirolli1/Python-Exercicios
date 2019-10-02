# Listas (Parte 2)
# Listas são mutáveis

teste = []
galera = []

teste.append('Matheus')
teste.append(23)
galera.append(teste[:])

teste[0] = 'Joice'
teste[1] = 23
galera.append(teste[:])
print(galera)

pessoas = [['João', 19], ['Joaquim', 13], ['Ana', 33], ['Maria', 45]]
for c in pessoas:
    print(c[0])

nomes = []
dado = []
for c in range(0, 3):
    dado.append(str(input('Digite nome: ')))
    dado.append(int(input('Digite idade: ')))
    nomes.append(dado[:])
    dado.clear()

for p in nomes:
    if p[1] >= 21:
        print(f'{p[0]} é Maior de Idade')
    else:
        print(f'{p[0]} é Menor de Idade.')
print(nomes)