salario = float(input())
novosalario = None
reajusteganho = None
empercentual = None
if salario <= 400:
    novosalario=((salario*0.15)+salario)
    reajusteganho = novosalario-salario
    empercentual = ('15 %')
elif salario >= 400.01 and salario <= 800:
    novosalario=(salario*1.12)
    reajusteganho = novosalario - salario
    empercentual = ('12 %')
elif salario >= 800.01 and salario <= 1200:
    novosalario=(salario*1.1)
    reajusteganho = novosalario - salario
    empercentual = ('10 %')
elif salario >= 1200.01 and salario <= 2000:
    novosalario=(salario*1.07)
    reajusteganho = novosalario - salario
    empercentual = ('7 %')
else:
    novosalario=(salario*1.04)
    reajusteganho = novosalario - salario
    empercentual =('4 %')
print('Novo salario: {:.2f}'.format(novosalario))
print('Reajuste ganho: {:.2f}'.format(reajusteganho))
print('Em percentual:', empercentual)