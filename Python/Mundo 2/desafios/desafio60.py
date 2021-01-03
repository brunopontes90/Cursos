print('===== desafio 59 ====='.upper())

# from math import factorial
# num = int(input('Digite para saber o Fatorial: '))
# fat = factorial(num)
# print('Fatorial de {} = {}'.format(num, fat))

num = int(input('Digite para saber o Fatorial: '))
cont = num
fat = 1
print('Calculando {}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print('{}'.format(fat))