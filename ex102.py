# Função para Fatorial

print('-=' * 15)


def fatorial(n, show=False):
    """
    Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opicional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} =', end=' ')
        f *= c
    return f


print(fatorial(5, show=True))
print('-=' * 15)

help(fatorial)

