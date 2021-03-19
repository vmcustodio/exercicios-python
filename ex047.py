#Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento
#Para salário superiores a R$1.250,00, calcule um aumento de 10%
#Para os inferiores ou iguais o aumento é de 15%
salario =float(input('Digite o valor do seu salario R$ '))
if salario>1250:
    novo=(1250*0.1)+salario
    print('o seu novo salario será de: R$', novo)
else:
    novo2 = (salario*0.15)+salario
    print(' o seu novo salario será de: R$', novo2)