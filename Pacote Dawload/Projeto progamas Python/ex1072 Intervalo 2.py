#Ex1072 Intervalo 2
entrada = int(input())
cont = 1
intervalo = 0
fora = 0
while cont <= entrada:
    numeros = int(input())
    if numeros >= 10 and numeros <= 20:
        intervalo = intervalo + 1
    else:
        fora = fora + 1
    cont = cont + 1
print('{} in\n{} out'.format(intervalo, fora))


