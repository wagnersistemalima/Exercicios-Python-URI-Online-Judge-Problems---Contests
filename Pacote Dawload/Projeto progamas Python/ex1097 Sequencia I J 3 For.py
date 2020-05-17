# ex1097 Sequencia I J 3
numero = 8
for c in range(1, 10, 2):       # O laço vai ate 9, pulando de 2 em 2. [1, 3, 5, 7, 9]
    for d in range(7, 4, -1):   
        numero = numero - 1             # controla a sequencia que é regressiva do numero 7 6 5
        print('I={} J={}'.format(c, numero))
    numero = numero + 5      # controla a mudança do número na repetição 7 6 5 numero + 5


