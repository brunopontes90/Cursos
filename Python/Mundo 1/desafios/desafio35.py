print('===== desafio 35 ====='.upper())
r1 = float(input('1º segmento: '))
r2 = float(input('2º segmento: '))
r3 = float(input('3º segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar triangulo')
else:
    print('Os seguimentos acima  podem formar triangulo')