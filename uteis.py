def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def dobro(n, formato=False):
    return n * 2 if formato is False else moeda(n * 2)


def triplo(n):
    return n * 3


def metade(n, formato=False):
    return n / 2 if formato is False else moeda(n / 2)


def porcentagem(n, formato=False):
    return n * 1.1 if formato is False else moeda(n * 1.1)


def porcentagemr(n, formato=False):
    return n * 0.9 if formato is False else moeda(n * 0.9)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')






