print('===== desafio 44 ====='.upper())

preco = float(input('Valor a pagar: '))
print('=' * 50)
print("""
ESCOLHA A FORMA DE PAGAMENTO
[1] Dinheiro ou Cheque
[2] A vista no credito
[3] Em ate 2x sem juros
[4] 3x ou mais com acrescimos de 20%'
""")
print('=' * 50)
opcao = int(input('Qual a forma de pagamento: '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 /100)
elif opcao == 3:    
    total = preco
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    tot_parcelas = int(input('Quantas parcelas? '))
    total = (preco + (preco * 20 / 100))
    parcelas = total / tot_parcelas
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(tot_parcelas, parcelas))
else:
    total = preco
    print('Opção invalida de pagamento, tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total))