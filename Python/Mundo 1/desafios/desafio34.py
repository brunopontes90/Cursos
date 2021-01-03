print('===== desafio 34 ====='.upper())
salario = float(input('Qual o seu salario: '))

if salario >= 1250:
    aumento = salario + (salario * 10 / 100)
    print('Seu salario com aumento R${:.2f}'.format(aumento))
else:
    aumento = salario + (salario * 15 / 100)
    print('Seu salario com aumento R${:.2f}'.format(aumento))