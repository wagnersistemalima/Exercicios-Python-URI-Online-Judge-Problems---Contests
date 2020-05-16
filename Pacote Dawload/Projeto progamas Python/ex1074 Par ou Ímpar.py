#ex1074 Par ou Ímpar
valores = int(input())
cont = 1
while cont <= valores:
    numero = int(input())
    if numero % 2 == 0 and numero > 0:
        print('EVEN POSITIVE')
    elif numero % 2 == 0 and numero < 0:
        print('EVEN NEGATIVE')
    if numero % 2 == 1 and numero > 0:
        print('ODD POSITIVE')
    elif numero % 2 == 1 and numero < 0:
        print('ODD NEGATIVE')
    if numero == 0:
        print('NULL')
    cont = cont + 1
