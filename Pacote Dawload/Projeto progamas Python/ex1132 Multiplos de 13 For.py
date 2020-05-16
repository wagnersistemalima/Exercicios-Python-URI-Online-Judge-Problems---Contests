# ex1132 Multiplos de 13
x = int(input())
y = int(input())

lista = []
lista.append(x)
lista.append(y)
lista.sort()                            # ordem crescente
x = lista[0]                            # x vai ser o menor numero
y = lista[1]                            # y vai ser o maior numero
inicio = x
fim = y

soma = 0
for c in range(inicio, fim + 1):
    if c % 13 != 0:
        soma = soma + c

print(soma)