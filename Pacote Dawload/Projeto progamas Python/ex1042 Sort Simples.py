# Ex1042 Sort Simples 10/04/2020
valor1, valor2, valor3 = map(int, input().split())
entrada1 = valor1
entrada2 = valor2
entrada3 = valor3
lista = []
lista.append(valor1)
lista.append(valor2)
lista.append(valor3)
lista.sort()
valor1 = lista[0]
valor2 = lista[1]
valor3 = lista[2]
print('{}\n{}\n{}'.format(valor1, valor2, valor3))
print('')
print('{}\n{}\n{}'.format(entrada1, entrada2, entrada3))