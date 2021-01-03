print('===== desafio 33 ====='.upper())
n1 = int(input('Digite 1º valor: '))
n2 = int(input('Digite 2º valor: '))
n3 = int(input('Digite 3º valor: '))

#VERIFICA QUAL O MAIOR
if n1 > n2 and n1 > n3:
    print('{} maior!'.format(n1))
elif n2 > n1 and n2 > n3:
    print('{} maior!'.format(n2))
elif n3 > n1 and n3 > n2:
    print('{} maior!'.format(n3))

#VERIFICA QUEM É O MENOR
if n1 < n2 and n1 < n3:
    print('{} menor!'.format(n1))
elif n2 < n1 and n2 < n3:
    print('{} menor!'.format(n2))
elif n3 < n1 and n3 < n2:
    print('{} menor!'.format(n3))