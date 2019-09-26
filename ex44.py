# Gerenciador de Pagamentos

print('===========LOJA FALCIROLLI============')
comp = float(input('Valor total das compras: '))
print('FORMAS DE PAGAMENTO'
'\n[1] à vista - dinheiro/cheque'
'\n[2] à vista - cartão'
'\n[3] 2x no cartão'
'\n[4] 3x ou mais no cartão')
op = int(input('Qual é a sua opção? '))
if op == 1:
    desc = comp * 0.9
    print('Sua compra de R${:.2f} receberá um desconto de 10%. Total a pagar final: R${:.2f}.'.format(comp, desc))
elif op == 2:
    print('Pagamento em 1x no cartão - à vista')
    print('Total a pargar: R${:.2f}'.format(comp))
elif op == 3:
    div = comp / 2
    print('Pagamento em 2x vezes no cartão - Sem juros.')
    print('Total a pagar: 2x de R${:.2f}'.format(div))
elif op == 4:
    n = int(input('Quantas parcelas? (Até 10x) '))

    i = 0.0250
    m = comp*((1+i)**n)
    j = m - comp
    parcela = m / n

    print('Sua compra será parcelada em {}x de R${:.2f} - Com juros compostos.'.format(n, parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(comp, m))
    print('Juros a pagar de 2.50% ao mês = R${:.2f}'.format(j))

else:
    print('Opção inválida. Tente novamente.')

