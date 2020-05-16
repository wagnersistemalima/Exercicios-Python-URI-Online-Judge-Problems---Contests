#Ex1066 pares, Ímpares, positivos, Negativos
valor = 1
pares = impares = positivo = negativo = 0
while valor <= 5:
    entrada = int(input())
    if entrada % 2 == 0:
        pares = pares + 1
    elif entrada % 2 == 1:
        impares = impares + 1
    if entrada > 0:
        positivo = positivo + 1
    elif entrada < 0:
        negativo = negativo + 1
    valor = valor + 1
print('{} valor(es) par(es)'.format(pares))
print('{} valor(es) impar(es)'.format(impares))
print('{} valor(es) positivo(s)'.format(positivo))
print('{} valor(es) negativo(s)'.format(negativo))