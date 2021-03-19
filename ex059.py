from datetime import date
atual = date.today().year
nascimento = int(input('qual ano de seu nascimento?: '))
idade = atual-nascimento
if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 25:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')