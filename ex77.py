# Contando Vogais em Tupla

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRÁTIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in palavras:
     print(f'\nNa palavra {c} temos', end=' ')
     for l in c:
         if l.lower() in 'aáãâàeéêiíóouú':
             print(l, end=' ')