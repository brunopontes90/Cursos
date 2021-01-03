print('===== desafio 38 ====='.upper())

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))

#VERIFICA SE AS VARIAVEIS SÃO IGUAIS E QUAL DELAS É A MAIOR
if n1 == n2:
    print('Não existe valor maior, os dois são iguais!')
elif n1 >  n2:
    print('{} é maior!'.format(n1))
else:
    print('{} é maior!'.format(n2))