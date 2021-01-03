# num = s = 0
# while True:
#     num = int(input('Digite um numero: '))
#     if num == 999:
#         break
#     s += num
# print('A soma vale {}'.format(s))
# print(f'A soma vale {s}')

# OUTROS EXEMPLOS DE f STRING:

nome = 'Bruno'
idade = 29
salario = 987.3
print(f'O {nome} tem {idade} anos e ganha {salario:.2f}') # PYTON 3.6+
print('O {} tem {} anos.'.format(nome, idade)) # PYTHON 3
print('O %s tem %d anos.' % (nome, idade)) # PYTHON 2