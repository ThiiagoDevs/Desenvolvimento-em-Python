'''Elabore um programa que calcule o valor a ser pago por um produto.'''
print('{:=^40}'.format('LOjas Dvs'))
preço = float(input('Preço das compras: R$ '))
print('''Forma de pagamento
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(
        'Sua compra será parcelada em 2x de R${:.2f}sem juros'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    tparc = int(input('Quantas parcelas? '))
    parcela = total / tparc
    print('Sua compra será em {}x de R${:.2f}com juros'.format(tparc, parcela))
else:
    total = preço
    print('OPÇÂO DE PAGAMNETO INVALIDA. TENDE NOVAMENTE! ')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(
    preço, total))
