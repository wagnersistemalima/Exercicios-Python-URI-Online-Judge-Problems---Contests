#ex1043 Triângulo 10/04/2020
a, b, c = map(float, input().split())
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    perimetro = a + b + c
    print('Perimetro = {}'.format(perimetro))
else:
    trapezio = ((a + b) * c) / 2
    print('Area = {}'.format(trapezio))