#Ex1071 Soma de impares consecultivos 1
valor1 = int(input())
valor2 = int(input())
lista = []
lista.append(valor1)
lista.append(valor2)
lista.sort(reverse=True)
valor1 = lista[0]
valor2 = lista[1]
inicio = valor2
fim = valor1
soma = 0
while inicio < fim:
    if inicio != valor2 and inicio % 2 == 1:
        soma = soma + inicio
    inicio = inicio + 1
print(soma)

