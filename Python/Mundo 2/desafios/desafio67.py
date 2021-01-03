print('===== desafio 67 ====='.upper())

while True:
    tabuada = int(input('Qual a tabuada: '))
    if tabuada < 0:
        break
    for i in range(0, 11):
        mult = tabuada * i
        print(f'{tabuada} x {i:2} = {tabuada * i:3}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!!!')