# Detector de  Palíndromo

fra = str(input('Digite uma frase: ')).strip().upper()
palavras = fra.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print(junto, inverso)
if inverso == junto:
    print('Palíndromo.')
else:
    print('Não é um Palíndromo.')
