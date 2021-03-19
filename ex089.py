#crie um programa que leia varios numeros inteiros pelo teclado, mostre a media entre todos e qual foi o maior e o menor valor.O programa deve perguntar ao usuario sele quer ou nao continuar a digitar valores
r = 'S'
soma =0
c = 0
media = 0
maior = 0
menor = 0
while r in 'Ss':
    n = int(input('Digite um valor: '))
    soma += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Deseja continuar? S/N'))
media = soma/c
print('Foram digitados {} numeros com o resultado da média entre eles de: {}, sendo o maior numero o {}, e o menor {}'.format(c,media,maior,menor))



