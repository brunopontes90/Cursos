print('===== desafio 66 ====='.upper())

n = c = s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    c += 1
    s += n
print (f'Ao todo foram digitados {c} valores e a soma entre eles é {s}')