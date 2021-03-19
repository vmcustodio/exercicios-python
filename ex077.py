# desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa mostre:
# a media de idade do grupo, qual o nome do homem mais velho, e quantas mulheres tem menos de 20 anos.
somaidade=0
medidade=0
maiorsexm=0
nomevelho = ''
sexm = 0
for p in range (1,5):
    print('-*-*-*-* {}ª PESSOA*-*-*-*-*-'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('Sexo: [F/M] ')).strip()
    somaidade = somaidade+idade
    if p ==1 and sexo in 'Mm':
        maiorsexm = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorsexm:
        maiorsexm = idade
        nomevelho = nome
    if sexo in'Ff' and idade < 20:
        sexm += 1
medidade = somaidade/4
print('A media de idade do grupo é de {} anos, já o homem mais velho é o {} com {} anos'.format(medidade, nomevelho,maiorsexm))
print('Por fim, o total de mulheres com menos de 20 anos é de {}'.format(sexm))