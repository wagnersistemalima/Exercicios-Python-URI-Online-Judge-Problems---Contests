#Ex 1073 Quadrado de Pares
valor = int(input())
cont = 1
while cont <= valor:
    if cont % 2 == 0:
        quadrado = cont**2
        print('{}^2 = {}'.format(cont, quadrado))
    cont = cont + 1
