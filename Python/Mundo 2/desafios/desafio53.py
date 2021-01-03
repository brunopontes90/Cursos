print('===== desafio 53 ====='.upper())

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # SEPARA EM UMA LISTA
junto = ''.join(palavras) # JUNTA TODAS AS PALAVRAS SEM ESPAÇO
inverso = junto[::-1] # FATIAMENTO
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palindromo!')