print('===== desafio 65 ====='.upper())

soma = quant = media = maior = menor = 0

res = 'S'
while res in 'Ss':
    num = int(input('Digite valor inteiro: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a media foi {}'.format(quant, media))
print('O maior foi {} e o menor foi {}'.format(maior, menor))

