# Dobro, Triplo e Raiz Quadrada

n = int(input('Digite um número: '))
db = n * 2
tp = n * 3
rq = n ** (1/2)
print('O dobro de {} é {}\nO triplo é {}\ne a Raiz Quadrada é {:.2f}'.format(n, (db), (tp), (rq)))

# Outra maneira utilizando apenas uma variável

n = int(input('Digite um número: '))
print('O dobro de {} é {}\nO triplo é {}\ne a Raiz Quadrada é {:.2f}'.format(n, (n*2), (n*3), (n**(1/2))))
