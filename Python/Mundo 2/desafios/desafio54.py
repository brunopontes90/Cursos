print('===== desafio 54 ====='.upper())
from datetime import date
atual = date.today().year
total_maior = 0
total_menor = 0
for pessoas in range(1, 8):
    nasc = int(input('Em qual ano a {}ª pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc
    if idade > 21:
        total_maior += 1
    else:
        total_menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(total_maior))    
print('E tivemos {} pessoas menores de idade'.format(total_menor))       