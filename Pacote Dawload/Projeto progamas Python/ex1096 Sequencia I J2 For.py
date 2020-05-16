# ex1096 Sequencia I J2
lista = [7, 6, 5]
subilista = [1, 3, 5, 7, 9]                  # range(1, 10) 1 a 9 saltiando de 2 em 2
for c in subilista:                          # para cada (c) número dentro da sublista
    for d in lista:                          # para cada (d) número dentro da lista mostre
        print('I={} J={}'.format(c, d))