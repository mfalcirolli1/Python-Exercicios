# Sistema interativo de ajuda em Python

from time import sleep

c = ('\033[m')

def ajuda(com):
    help(com)


comando = ''
while True:
    print('~' * 25)
    print(' SISTEMA DE AJUDA PyHELP')
    print('~' * 25)
    sleep(1)
    comando = str(input('Função ou Biblioteca >> ')).strip()
    sleep(1)
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
        sleep(1)
print('Até logo.')