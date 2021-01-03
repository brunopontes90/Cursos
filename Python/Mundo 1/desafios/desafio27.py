print('===== desafio 27 ====='.upper())

nome_completo = str(input('Digite seu nome completo: ')).strip()
nome = nome_completo.split()
print('Primeiro nome: {}'.format(nome[0]))
print('Ultimo nome: {}'.format(nome[len(nome)]-1))    