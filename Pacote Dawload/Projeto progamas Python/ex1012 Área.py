#ex1012 Área 09/04/2020
a, b, c = map(float, input().split())  # Função map aplica uma função a todos elementos de uma sequência
triangulo = a * c / 2
pi = 3.14159
circulo = pi * c**2
trapezio = ((a + b) * c) / 2
quadrado = b**2
retangulo = a * b
print('TRIANGULO: {:.3f}'.format(triangulo))
print('CIRCULO: {:.3f}'.format(circulo))
print('TRAPEZIO: {:.3f}'.format(trapezio))
print('QUADRADO: {:.3f}'.format(quadrado))
print('RETANGULO: {:.3f}'.format(retangulo))
