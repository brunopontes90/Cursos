print('===== desafio 52 ====='.upper())

num = int(input('Digite um valor: '))
mult = 0

for i in range(2, num + 1):
    if num % i == 0:
        print('\033[31m', end=" ")
        mult += 1
print('\n\033[mO numero {} foi divisivel {}x'.format(num, mult))
if mult == 2:
    print('É primo')
else:
    print('Não é primo')