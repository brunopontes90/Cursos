print('===== desafio 39 ====='.upper())

from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year

idade = ano_atual - nascimento

print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, ano_atual))

#VERIFICA SE JA PASSOU O ALISTAMENTO OU QUANTO TEMPO FALTA
if idade < 18:
    tempo = 18 - idade
    ano = ano_atual + tempo
    print('Ainda ira se alistar, falta {} anos!'.format(tempo))
    print('Seu alistamento sera em {}'.format(ano))
elif idade == 18:
    print('Precisa se alistar, esta na hora!')
else:
    tempo = idade - 18
    ano = ano_atual - tempo
    print('Já passou do tempo de alistamento a {} anos'.format(tempo))
    print('Seu alistamento foi em {}'.format(ano))