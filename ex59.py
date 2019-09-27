# Criando um Menu de Opções

p1 = float(input('Primeiro número: '))
p2 = float(input('Segundo número: '))

op = 0
while op != 5:
    print('   [1] Somar')
    print('   [2] Multiplicar')
    print('   [3] Qual é o Maior')
    print('   [4] Inserir novos números')
    print('   [5] Sair do programa')
    op = int(input('>>>>> Qual é a sua opção? '))

    if op == 1:
        s = p1 + p2
        print('{} + {} = {}'.format(p1, p2, s))


    elif op == 2:
        m = p1 * p2
        print('{} x {} = {}'.format(p1, p2, m))


    elif op == 3:
        if p1 > p2:
            print('{} é o MAIOR número.'.format(p1))
        else:
            if p2 > p1:
                print('{} é o MAIOR número.'.format(p2))


    elif op == 4:
        print('Informe os números novamente: ')
        p1 = float(input('Primeiro número: '))
        p2 = float(input('Segundo número: '))

    elif op == 5:
        print('Finalizando...')

    else:
        print('Opção inválida. Tente novamente.')


print('Operação finalizada com sucesso! Obrigado por utilizar o nosso sistema.')