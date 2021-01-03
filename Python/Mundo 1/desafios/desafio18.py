from math import  radians, sin,cos,tan
print('===== desafio 1 ====='.upper())

#SOLICITA O ANGULO, TRANFORMA EM RADIANOS E CALCULA O SENO, COSSENO E TANGENTE
angulo = float(input('Digite o angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('Seno: {:.2f}\n Cosseno {:.2f}\n Tangente: {:.2f}'.format(seno,cosseno,tangente))