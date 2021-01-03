print('===== desafio 76 ====='.upper())

produtos = ('Lapis', 1.75, 
            'Borracha', 2, 
            'Caderno', 5.90,
            'Estojo', 10.50,
            'Mochila', 125.50,
            'Livro', 27.50)
print('-' * 40) 
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-' * 40)