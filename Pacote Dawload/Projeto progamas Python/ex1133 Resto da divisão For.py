#ex1133 Resto da divisão
x = int(input())
y = int(input())

lista = []
lista.append(x)
lista.append(y)
lista.sort()
x = lista[0]                            # x vai ser o menor numero
y = lista[1]                            # y vai ser o maior numero
inicio = x
fim = y

for c in range(inicio + 1, fim):
    if c % 5 == 2 or c % 5 == 3:
        print(c)
