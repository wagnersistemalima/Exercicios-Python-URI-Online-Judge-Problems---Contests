#ex1048 Aumento de Sálario
entrada = float(input())
if entrada <= 400.00:
    salario = entrada * 0.15 + entrada
    a = entrada * 0.15
    print('Novo salario: {:.2f}'.format(salario))
    print('Reajuste ganho: {:.2f}'.format(a))
    print('Em percentual: 15 %')
if entrada > 400.00 and entrada <= 800.00:
     salario = entrada * 0.12 + entrada
     a = entrada * 0.12
     print('Novo salario: {:.2f}'.format(salario))
     print('Reajuste ganho: {:.2f}'.format(a))
     print('Em percentual: 12 %')
if entrada > 800.00 and entrada <= 1200.00:
    salario = entrada * 0.10 + entrada
    a = entrada * 0.10
    print('Novo salario: {:.2f}'.format(salario))
    print('Reajuste ganho: {:.2f}'.format(a))
    print('Em percentual: 10 %')
if entrada > 1200.00 and entrada <= 2000.00:
    salario = entrada * 0.07 + entrada
    a = entrada * 0.07
    print('Novo salario: {:.2f}'.format(salario))
    print('Reajuste ganho: {:.2f}'.format(a))
    print('Em percentual: 7 %')
if entrada > 2000.00:
    salario = entrada * 0.04 + entrada
    a = entrada * 0.04
    print('Novo salario: {:.2f}'.format(salario))
    print('Reajuste ganho: {:.2f}'.format(a))
    print('Em percentual: 4 %')








