print('===== desafio 59 ====='.upper())

from time import sleep
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
opcao = 0

while opcao != 5:
    print("""
    ----------------------------
    ESCOLHA A OPÇÃO DESEJADA:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Numeros
    [5] Sair do Programa
    ---------------------------
    """)

    opcao = int(input('>>>>> Escolha a opção: '))
        
    if opcao == 1:
        soma = n1 + n2
        print('{} + {}  = {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('{} x {} = {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2 
        print('O maior entre {} e {} é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os numeros novamente:')
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
    elif opcao == 5:
        print('finalizando...'.upper())
        sleep(1)
    else:
        print('Opção invalida. Tente novamente')
print('Fim do programa, volte sempre!')