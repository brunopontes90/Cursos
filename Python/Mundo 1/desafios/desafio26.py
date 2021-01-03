print('===== desafio 26 ====='.upper())

frase = str(input('Digite uma frase: ')).upper().strip()


print('Quantas vezes aparece a letra "A": {}'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição: {}'.format(frase.find('A')+1))
print('A ultima letra "A" apareceu na posição: {}'.format(frase.rfind('A')+1)) #PROCURA DO LADO DIREITO