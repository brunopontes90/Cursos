print('===== desafio 36 ====='.upper())


casa = float(input('Valor do imovel: '))
salario = float(input('Seu salario: '))
anos = int(input('Quanto tempo deseja pagar(anos): '))

prestacao = casa / (anos * 12) #CALCULA A PARCELA DO IMOVEL
minimo = salario * 30 / 100 #CALCULA 30% DO SALARIO DO COMPRADOR
print('Para pagar a casa  de R${:.2f} em {} anos'.format(casa, anos), end="")
print(' a prestação sera de R${:.2f}'.format(prestacao))

#VERIFICA SE A PARCELA É MENOR QUE O MINIMO DE 30% DO SALARIO
if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO!')