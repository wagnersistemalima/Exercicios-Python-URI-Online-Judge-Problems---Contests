#Ex 1013 O Maior  09/04/2020. Utilizando lista
a, b, c = map(int, input().split())
lista = []
lista.append(a)      # acrecentando os numeros na lista .append
lista.append(b)
lista.append(c)
lista.sort(reverse=True)  # Ordenando os numeros na lista em ordem decrecente, do maior para o menor
a = lista[0]
b = lista[1]
c = lista[2]
print('{} eh o maior'.format(a))

