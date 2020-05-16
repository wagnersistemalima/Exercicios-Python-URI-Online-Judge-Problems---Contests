#ex1051  Imposto de Renda.
entrada = float(input())
if entrada >= 0.00 and entrada <= 2000.00:
    print('Isento')
if entrada > 2000.00 and entrada <= 3000.00:
    entrada = entrada - 2000.00
    i = entrada * 0.08
    print('R$ {:.2f}'.format(i))
if entrada > 3000.00 and entrada <= 4500.00:
    entrada = entrada - 3000.00
    i = entrada * 0.18 + 80
    print('R$ {:.2f}'.format(i))
if entrada > 4500.00:
    entrada = entrada - 4500.00
    i = entrada * 0.28 + 350
    print('R$ {:.2f}'.format(i))


