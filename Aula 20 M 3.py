# Funções (Parte 1)

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A + B = {s}')


soma(b=4, a=5)

# a = 8
# b = 9
# s = a + b
# print(s)


def contador(*num):
    tam = len(num)
    print(num)
    print(f'Recebi os valores {num}. Ao todo são {tam} números.')


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)


valores = [6, 3, 9, 1, 0, 2]
def dobra(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1

dobra(valores)
print(valores)
