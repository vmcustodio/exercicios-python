#faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lidos
maior = 0
menor = 1000
for p in range(1,6):
    a = float(input('Digite o peso em KG: '))
    if a == 1:
        maior = a
        menor = a
    else:
        if a > maior:
            maior = a
        if a < menor:
            menor = a
print(' O menor peso é de {}Kg, enquanto o maior peso é de {}Kg'.format(menor,maior))