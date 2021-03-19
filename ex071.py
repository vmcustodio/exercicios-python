#desensvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. se o valor digitado for impar, desconsidere-o
soma = 0
for c in range (1,7):
    a = int(input('Digite um numero: '))
    if a%2==0:
        soma += a
print('A soma dos numeros pares é', soma)