#Tipos Primitivos
#str, float, bool, int

n = input('Digite um valor: ')
print(n.isupper())

#Desafios (Aula 6)
#1
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
m = n1 + n2
print('A soma entre {} e {} é igual a {}!'.format(n1, n2, m))

#2
m = input('Digite algo aleatóriamente: ')
print('O tipo primitivo desse valor é:', type(m))
print('Está em letra maiúcula:', m.isupper())
print('Contêm apenas números:', m.isnumeric())
print('Contêm apenas letras:', m.isalpha())
print('Está em letra minúscula:', m.islower())
print('É alfanumérico:', m.isalnum())
print('É copiável:', m.isprintable())



