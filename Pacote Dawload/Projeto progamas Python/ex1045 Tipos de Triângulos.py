#1045  Tipos de Triângulos 10/04/2020
a, b, c = map(float, input().split())
lista = []
lista.append(a)
lista.append(b)
lista.append(c)
lista.sort(reverse=True)
a = lista[0]
b = lista[1]
c = lista[2]
if a >= b + c:
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')
    if a**2 > b**2 + c**2:
        print('TRIANGULO OBTUSANGULO')
    if a**2 < b**2 + c**2:
        print('TRIANGULO ACUTANGULO')
    if a == b and b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c:
        print('TRIANGULO ISOSCELES')




