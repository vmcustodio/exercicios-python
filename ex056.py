#escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
#o primeiro valor é maior, o segundo valor é maior, não existe valor maior, os dois são iguais
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um segundo numero: '))
if n1>n2:
    print('o primeiro numero é maior')
elif n1<n2:
    print('o segundo numero é maior')
else:
    print('Os dois numeros são iguais')