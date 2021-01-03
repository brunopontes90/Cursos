print('===== desafio 70 ====='.upper())
total = totmil = menor = cont =  0
barato = ''
while True:
    # SOLICITA PRODUTO E VALOR E SOMA TODOS
    produto = str(input('Nome do produto: ')).strip().capitalize()
    preco = float(input('Valor do produto: R$'))
    cont += 1

    # VERIFICA QUANTOS PRUDOTOS SÃO MAIORES QUE MIL REIAS
    total += preco
    if preco > 1000:
        totmil += 1

    # VERIFICA QUAL O PRODUTO DE MENOR VALOR
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    
    # PERGUNTA SE DESEJA CONTINUAR, CASO DIGITE 'N' O PROGRAMA PARA
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break


print('{:-^40}'.format(' FIM DO PROGRAMA '))

print(f'Total da compra: R${total:.2f}')
print(f'Quantidade de produtos maiores que R$ 1.000,00: {totmil}')
print(f'Produto mais barato foi {barato} que custa: R${menor:.2f}')