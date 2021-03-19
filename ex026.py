import random
aluno1 = input('digite o nome do aluno:')
aluno2 = input('digite o nome do aluno')
aluno3 = input('digite o nome do aluno')
aluno4 = input('digite o nome do aluno')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print ('o aluno escolhido foi {}'.format(escolhido))
