# Um print especial

def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)

escreva('Olá')
escreva('Tudo bem')
escreva('Matheus Santos Falcirolli')