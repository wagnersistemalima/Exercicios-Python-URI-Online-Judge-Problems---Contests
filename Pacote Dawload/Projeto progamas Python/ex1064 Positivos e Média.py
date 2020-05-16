#ex1064 Positivo e média
valor = 1
positivo = 0
media = 0
soma = 0
while valor <= 6:
    entrada = float(input())
    if entrada > 0:
        positivo = positivo + 1
        soma = soma + entrada
        media = soma / positivo
    valor = valor + 1
print('{} valores positivos'.format(positivo))
print('{:.1f}'.format(media))

