n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))
m = (n1 + n2) / 2
print('A sua media foi {:.1f}'.format(m))

if m >= 6:
    print('APROVADO!')
else:
    print('REPROVADO!')

#print('Parabens' if m >= 6 else 'Estude mais')
#IF ELSE SIMPLIFICADO