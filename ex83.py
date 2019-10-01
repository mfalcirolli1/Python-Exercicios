# Validando expressões matemáticas

c = 0
d = 0
exp = str(input('Digite a expressão: '))
pilha = []
for s in exp:
    if s == '(':
        c += 1
    elif s == ')':
        d += 1

if d == c:
    print('Expressão Válida!')
else:
    print('Expressão Inválida!')