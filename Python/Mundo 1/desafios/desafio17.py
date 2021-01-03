from math import hypot
print('===== desafio 17 ====='.upper())

#SOLICITA O CATETO OPOSTO E CATETO ADJACENTE
cat_oposto = float(input('Digite o cateto oposto: '))
cat_adjacente = float(input('Digite o cateto adjacente: '))

#CALCULA A HIPOTENUSA RECEBENDO OS CATETOS ADJACENTE E OPOSTO   
hipotenusa = hypot(cat_oposto, cat_adjacente)
print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))

#MANEIRA MATEMATICA
#hipotenusa = (cat_oposto ** 2 + cat_adjacente ** 2) ** (1/2)
#