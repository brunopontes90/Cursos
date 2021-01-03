print('===== desafio 44 ====='.upper())

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Abaixo do Peso!')
elif imc >= 18.5 and imc < 25:
    print('Indice de Massa Corporea: {:.1f}'.format(imc))
    print('Peso Ideal!')
elif imc >= 25 and imc < 30:
    print('Indice de Massa Corporea: {:.1f}'.format(imc))
    print('Sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Indice de Massa Corporea: {:.1f}'.format(imc))
    print('Obesidade!')
else:
    print('Indice de Massa Corporea: {:.1f}'.format(imc))
    print('Obesidade Morbida!')