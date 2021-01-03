print('===== desafio 49 ====='.upper())
num = int(input('Qual a tabuada: '))
for i in range(0, 11):
    print('{} x {:2} = {}'.format(num, i, num * i))