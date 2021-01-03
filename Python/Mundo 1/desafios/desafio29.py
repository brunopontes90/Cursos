print('===== desafio 29 ====='.upper())
vel = int(input('Digite a velocidade de seu veiculo em KM/h: '))

if vel > 80:
    m = (vel - 80) * 7 #CALCULA O VALOR A CIMA DOS 80   
    print('Você ultrapassou o limite!')
    print('Tera que pagar uma multa de R${:.2f}'.format(m))
print('Parabens, dentro da velocidade!')#PODEMOS USAR SEM ELSE