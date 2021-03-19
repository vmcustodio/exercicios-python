#crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final, mostres quantos numeros foram digitados e qual foi a soma entre eles,desconsiderando o 999
n = 0
c = 0
soma = 0
n = int(input('Digite um numero ou 999 para parar: '))
while n != 999:
    c +=1
    soma += n
    n = int(input('Digite um numero ou 999 para parar: '))
print('Foram digitados {} valores, com a soma entre eles de {}'.format(c,soma))
print('Fim')