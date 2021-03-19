#faça um programa que leia um ano qualquer e mostre se ele é bissexto
ano = int(input('digite um ano: '))
if (ano%4)==0 and (ano%400)==0:
    print('é um ano bissexto')
else:
    (ano%100)==0
    print('não é um ano bissexto')

