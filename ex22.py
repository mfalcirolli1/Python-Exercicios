# Analisador de textos
nome = input('Digite seu nome: ').strip()
sep = nome.split()

print('Analisando o seu nome...')
print('Seu nome em letras maiúsculas é: {}.'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(sep[0], len(sep[0])))
print('Seu nome do meio é {} e ele tem {} letras.'.format(sep[1], len(sep[1])))
print('Seu último nome é {} e ele tem {} letras.'.format(sep[2], len(sep[2])))
