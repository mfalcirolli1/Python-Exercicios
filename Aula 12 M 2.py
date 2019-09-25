# Condições aninhadas

nome = str(input('\033[1;36mQual é o seu nome?\033[m '))
if nome == 'Matheus':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Joice':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Juliana':
    print('Belo nome feminino')
else:
    print('Bonito nome!')
print('Tenha um bom dia, {}!'.format(nome))
