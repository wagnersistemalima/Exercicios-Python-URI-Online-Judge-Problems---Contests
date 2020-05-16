# EX1099 Soma de impares consecutiovos 2
quantidade_casos = int(input())
for b in range(1, quantidade_casos + 1):
    x, y = map(int, input().split())
    lista = []
    lista.append(x)
    lista.append(y)
    lista.sort(reverse=True)
    x = lista[0]                                                   # x é o maior numero
    y = lista[1]                                                   # y é o menor numero
    soma = 0
    inicio = y
    fim = x
    for c in range(inicio + 1, fim):
        if c % 2 == 1:
            soma = soma + c
    print(soma)
