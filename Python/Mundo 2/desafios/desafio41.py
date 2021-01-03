print('===== desafio 41 ====='.upper())

from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
data = date.today().year

idade = data - nascimento

if idade < 9:
    print('Atleta Mirim, tem {} anos'.format(idade))
elif idade >= 9 and idade < 14:
    print('Atleta Infanfil, tem {} anos'.format(idade))
elif idade >= 14 and idade < 19:
    print('Atleta Junior, tem {} anos'.format(idade))
elif idade >= 19 and idade <=20:
    print('Atleta Senior, tem {} anos'.format(idade))
else:
    print('Atleta Master, tem {} anos'.format(idade))