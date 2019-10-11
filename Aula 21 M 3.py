# Funções (Parte 2)

# help(input)
# print(input.__doc__)


def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela.
    :param i: Ínicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    Criado por Matheus S. Falcirolli
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')


contador(10, 100, 5)
help(contador)


def somar(a=0, b=0, c=0):
    """
    Parâmetros Opcionais
    """
    s = a + b + c
    print(f'{s}')


somar(1200, 1307)
help(somar)


def funcao():
    """
    Escopo de variáveis
    """
    a = 4
    print(f'Dentro {a}')


a = 5
funcao()
print(f'Fora {a}')


def somar2(a=0, b=0, c=0):
    """
    Return
    """
    s = a + b + c
    return s


r1 = somar2(3, 2, 5)
r2 = somar2(2, 2)
r3 = somar2(6)
print(f'{r1} {r2} {r3}')


def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'{n}! = {fatorial(n)}')
