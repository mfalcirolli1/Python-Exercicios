# Manipulando Texto

f = 'curso em vídeo python'
print(f[15:])

# [:5] - [15:] - [9:14] - [9::3] = [9:21:3]

print('O comprimento da frase é de: {} caracteres'.format(len(f)))  #Comprimento
print(len(f))
print(f.count('o', 0, 21)) #Contador de caracteres
print(f.find('y')) #Localizador de caractere em relação ao comprimento
print('Curso' in f) #Teste de existência
print('Android' in f) #Teste de existência
print(f.replace('python', 'Android')) #Substituir
print(f.upper()) #Maiúsculo
print(f.lower()) #Minúsculo
print(f.capitalize()) #Primeira letra da frase maiúscula
print(f.title()) #Primeira letra de todas as palavras maiúsculi
print(f.strip()) #Remove espaços vazios no começo e no fim da str (rstrip / lstrip)
print(f.split()) #Divisão das palavras as colocando em lista
print('-'.join(f)) #Junção

dividido = f.split()
print(dividido[0][2])






# loc = input('Digite uma letra presente na frase para saber a sua localização numérica: ')
# print('A letra digitada {}, está na posição {}'.format(loc, f.find(loc)))