#crie um programa que leia dois valores e mostre um menu na tela:
#[1]somar,[2]multiplicar,[3]maior,[4]novos numeros,[5]sair do programa. seu programa devera realizar a operação solicitada em cada caso.
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
x = 0
while x != 5:
    print ('''   ---------------
    OPÇÕES:
    [1]somar
    [2]multiplicar
    [3]maior
    [4]novos numeros
    [5]sair do programa
    -------------------''')
    x = int(input('Digite a opção desejada:'))
    if x == 1:
        print('O resultado da soma é de: ', n1+n2)
    elif x==2:
        print('O resultado da multiplicação é de', n1*n2)
    elif x==3:
        if n1>n2:
            print('O maior numero é', n1)
        else:
            print('O maior numero é',n2)
    elif x == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif x == 5:
        print('Obrigada!')
    else:
        print('A opção que você digitou é invalida')
print('Fim' )

