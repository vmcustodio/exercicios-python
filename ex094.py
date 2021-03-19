#faça um programa que leia a idade e o sexo de varias pessoas. a cada pessoa cadastrada, o programa devera perguntar se o usuario quer continuar. no final mostre:
#quantas pessoas tem mais de 18 anos, quantos homens foram cadastrados,quantas mulheres tem menos de 20 anos
idade2 = 0
homem = 0
mulherid = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: ')).strip().upper()
    if idade > 18:
        idade2 +=1
    if sexo == 'M':
        homem +=1
    if sexo == 'F' and idade <20:
        mulherid +=1
    resp = ' '
    while resp not in'SN':
        resp = str(input('Deseja continuar? [s/n] ')).strip().upper()
    if resp == 'N':
        break
print(f'Infomações: Foram cadastradas {idade2} pessoas com mais de 18 anos. Ao todo, foram cadastrados {homem} homens, e {mulherid} mulher(es) com idade abaixo de 20 anos')



