print('===== desafio 04 ====='.upper())
ler = input('Digite algo: ')
print('O tipo primitivo é? ', type(ler))
print('É alfabetico? ', ler.isalpha())
print('É alfa numerico? ', ler.isnumeric())
print('Pode ser impresso? ', ler.isprintable())
print('É apenas numeros? ',  ler.isnumeric())
print('Esta em minusculo? ', ler.islower())
print('Esta em maiusculo? ', ler.isupper())
print('Somente espaços? ', ler.isspace())
print('Esta capitalizada (Titulo)? ', ler.istitle())