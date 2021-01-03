print('===== desafio 69 ====='.upper())

idade = total18 = totalH = totalM20 =  0

while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        total18 += 1

    if sexo == 'M':
        totalH += 1

    if sexo == 'F' and idade < 20:
        totalM20 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    
    if continuar == 'N':
        break

print(f'Total de pessoas maiores de 18 anos: {total18}')
print(f'Total de homens: {totalH}')
print(f'Total de mulheres menores de 20 anos: {totalM20}')