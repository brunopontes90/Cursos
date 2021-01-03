from random import shuffle
print('===== desafio 20 ====='.upper())

#SOLICITA 4 NOMES
aluno1 = input('1º aluno, digite seu nome: ')
aluno2 = input('2º aluno, digite seu nome: ')
aluno3 = input('3º aluno, digite seu nome: ')
aluno4 = input('4º aluno, digite seu nome: ')

lista = [aluno1, aluno2, aluno3, aluno4] #CRIA UMA LISTA COM OS NOMES
shuffle(lista) #EMBARALHA OS NOMES
print('A ordem de apresentação sera:')
print(lista)


