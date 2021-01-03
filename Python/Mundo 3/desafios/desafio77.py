print('===== desafio 76 ====='.upper())

palavras = ('aprender', 'programar', 'linguagem',
            'python', 'curso', 'gratis', 'praticar', 
            'trabalhar', 'mercado', 'programador', 'futuro')

# PEGA CADA PALAVRA DA TUPLA
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    # VERIFICA SE NA PALAVRA POSSUI 'A E I O U' E IMPRIME
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')