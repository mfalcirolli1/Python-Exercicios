# Par ou Ímpar
num = int(input('\033[1;31mDigite um número inteiro para saber se ele é par ou ímpar:\033[m '))
result = num % 2
if result == 0:
    print('{} é \033[1;35mpar\033[m!'.format(num))
else:
    print('{} é \033[1;36mímpar\033[m!'.format(num))

