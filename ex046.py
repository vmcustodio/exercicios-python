#faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor
n1 = float(input('Digite o 1º numero: '))
n2 = float(input('Digite o 2º numero: '))
n3 = float(input('Digite o 3º numero: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3 < n2:
    menor = n3
maior = n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
print('o menor valor digitado foi',menor)
print('o maior valor digitado foi', maior)
