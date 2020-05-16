# ex1095 Sequencia i j1
numero = 1
for c in range(60, -1, -5):     # para cada número entre 0, 60, faça a contagem regressiva de 60, saltiando de 5 em 5
    print('I={} J={}'.format(numero, c))
    numero = numero + 3         # Numero começa com 1, salta de 3 em 3, ate a contagem regressiva chegar a 0