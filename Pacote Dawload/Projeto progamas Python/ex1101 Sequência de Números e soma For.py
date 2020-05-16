# Ex 1101 sequencia de números e soma
while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    lista = []
    lista.append(m)                                  # Adiciona na lista no final
    lista.append(n)                                  # Adiciona na lista no final
    lista.sort(reverse=True)                         # Organiza a lista em ordem decrescente, do maior para o menor
    m = lista[0]                                     # m vai ser o maior
    n = lista[1]                                     # n vai ser o menor
    inicio = n
    fim = m
    soma = 0
    for c in range(inicio, fim + 1):
        soma = soma + c
        print('{}'.format(c), end=' ')
    print('Sum=', end='')
    print('{}'.format(soma), end='')
    print()



