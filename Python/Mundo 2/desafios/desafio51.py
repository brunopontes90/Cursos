print('===== desafio 51 ====='.upper())
termo1 = int(input('1º termo: '))
razao = int(input('Razão: '))
decimo = termo1 + (10 - 1) * razao
for i  in range(termo1, decimo + razao, razao):
    print('{}'.format(i), end=" -> ")
print('ACABOU')