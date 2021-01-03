print('===== desafio 40 ====='.upper())

n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))

media  = (n1 + n2) / 2 #SOMA AS NOTAS E DIVIDE POR 2

print('Tirando {} e {} sua media é {}'.format(n1, n2, media))

#VERIFICA SE O ALUNO ESTA REPROVADO, EM RECUPERAÇÃO OU APROVADO
if media < 5.0:
    print('REPROVADO!')
    print('Sua media foi {:.1f}'.format(media))
elif media >= 5.0 and media <= 5.9:
    print('RECUPERAÇÃO!')
    print('Sua media foi {:.1f}'.format(media))
else:
    print('APROVADO!')