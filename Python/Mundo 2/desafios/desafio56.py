print('===== desafio 56 ====='.upper())
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
tot_mulher = 20
for pessoa in range(1,5):
    print('----- {}ª pessoa -----'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).split()
    soma_idade += idade
    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and tot_mulher < 20:
        tot_mulher += 1
media_idade = soma_idade / 4
print('A media de idade do grupo é de {} anos'.format(media_idade))
print('O homem mais velho tem {} e se chama {}.'.format(maior_idade_homem, nome_mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(tot_mulher))