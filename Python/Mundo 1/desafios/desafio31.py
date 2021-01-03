print('===== desafio 31 ====='.upper())
viagem = float(input('Digite a distancia da viagem em KM: '))

if viagem <= 200:
    preco = viagem * 0.50
    print('Sua passagem saira no valor de R${:.2f}'.format(preco))
else:
    preco = viagem * 0.45
    print('Sua passagem saira no valor de R${:.2f}'.format(preco))
