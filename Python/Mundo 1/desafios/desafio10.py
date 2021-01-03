print('===== desafio 10 ====='.upper())
reais = float(input('Digite o valor em reais: '))
dolar = reais / 3.27
print('Com: R${} reais\n Você pode comprar US${:.2f} dolares'.format(reais, dolar))