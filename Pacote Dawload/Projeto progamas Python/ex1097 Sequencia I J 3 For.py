# ex1097 Sequencia I J 3
numero = 8
for c in range(1, 10, 2):       # O laço vai ate 9, pulando de 2 em 2. [1, 3, 5, 7, 9]

    for d in range(7, 4, -1):   # o valor do numero decrece, 7, 6, 5 ai ... volta pra o outro laço
        numero = numero - 1
        print('I={} J={}'.format(c, numero))
    numero = numero + 5         # Quando começa o outro laço o numero está em 5 + aumenta 5= 10 -1 começa 9, 8, 7


