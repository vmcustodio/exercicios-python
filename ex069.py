#faça um programa que calcule a soma entre todos os numeros impares que são multiplos de tres e que se encontram no intervalo de 1 ate 500
soma = 0
cont = 0
for c in range(1,500,2):
    if c % 3 ==0:
        print(c, end = ' ')
    if c%3==0:
      cont = cont + 1
      soma = soma + c
print('\n a soma dos {} valores é igual {}'.format(cont, soma))