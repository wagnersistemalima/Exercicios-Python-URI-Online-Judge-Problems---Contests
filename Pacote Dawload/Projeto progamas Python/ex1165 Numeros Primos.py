casos = int(input())
inicio = 1
while inicio <= casos:
    entrada = int(input())
    inicio = inicio + 1
    divisor = 2
    contador = 0
    comeca = 1
    while divisor < entrada:
        if entrada % divisor == 0:
            contador = contador + 1
        divisor = divisor + 1
    if contador == 0:
        print('{} eh primo'.format(entrada))
    else:
        print('{} nao eh primo'.format(entrada))


