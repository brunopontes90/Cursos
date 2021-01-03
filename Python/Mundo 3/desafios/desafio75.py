print('===== desafio 75 ====='.upper())
numeros = (int(input('Digite um valor: ')), 
        int(input('Digite outro valor: ')), 
        int(input('Digite mais um valor: ')), 
        int(input('Digite o ultimo valor: ')))

print(f'Você digitou os numeros: {numeros}')
print(f'O valor 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 esta na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram:', end='')
for num in numeros:
    if num % 2 == 0:
        print(num, end=' ')

