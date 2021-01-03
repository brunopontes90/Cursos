print('===== desafio 42 ====='.upper())
r1 = float(input('1º segmento: '))
r2 = float(input('2º segmento: '))
r3 = float(input('3º segmento: '))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('Os seguimentos acima podem formar um triangulo ', end="")
    if (r1 == r2) and (r2 == r3): #OUTRA FORMA: R1 == R2 == R3
            print('Triangulo Equilátero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os seguimentos acima não podem formar triangulo')