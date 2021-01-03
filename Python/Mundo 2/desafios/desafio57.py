print('===== desafio 57 ====='.upper())
sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

# VERIFICA SE O DIGITADO ESTA CORRETO
while sexo not  in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor digite seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))