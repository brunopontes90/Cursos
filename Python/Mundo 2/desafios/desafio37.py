print('===== desafio 37 ====='.upper())

num = int(input('Digite valor inteiro: '))
print("""
Escolha umas das bases para conversão:
[1] converter para BINARIO
[2] converter para OCTAL
[3] conveter para HEXADECIMAL
""")
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(opcao, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(opcao, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(opcao, hex(num)[2:]))
else:
        print('Opção invalida!!')