print('===== desafio 22 ====='.upper())

nome = input('Digite seu nome completo: ').strip()

print('Nome em maiusculas: {}'.format(nome.upper()))
print('Nome em minusculas: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))#remove os espaços
separar = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separar[0], len(separar[0])))