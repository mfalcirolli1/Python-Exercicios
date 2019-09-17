# Condições Simples e Composta

#Simples
nome = str(input('Qual é o seu nome? '))
if nome == 'Matheus':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))

#Composta
nome = str(input('\033[7;30mQual é o seu nome?\033[m '))
if nome == 'Matheus':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é comum.')
print('Bom dia, \033[1;34m{}\033[m!'.format(nome))

#Exemplo
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2

print('Média igual a: {:.2f}'.format(m))
if m >= 6:
    print('Aprovado')
else:
    print('Reprovado')

print('Aprovado' if m >=6 else 'Reprovado')