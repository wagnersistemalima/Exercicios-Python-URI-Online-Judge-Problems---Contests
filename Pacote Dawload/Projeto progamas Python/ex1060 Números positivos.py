# Ex 1060 Números positivos.
cont = 1
positivo = 0
while cont <= 6:
    valor = float(input())
    if valor > 0:
        positivo = positivo + 1
    cont = cont + 1
print('{} valores positivos'.format(positivo))



