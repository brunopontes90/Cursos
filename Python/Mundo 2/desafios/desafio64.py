print('===== desafio 64 ====='.upper())

num = cont = soma = 0
num = int(input('Digite um numero [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para parar]: '))
   
print('Você digitou {} e a soma entre eles foi {}.'.format(cont, soma))

    
