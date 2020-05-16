#Ex1065 Pares entre Cinco Números
valor = 1
par = 0
while valor <= 5:
    entrada = int(input())
    if entrada % 2 == 0:
        par = par + 1

    valor = valor + 1
print('{} valores pares'.format(par))