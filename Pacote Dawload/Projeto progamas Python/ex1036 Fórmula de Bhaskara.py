#1036 Fórmula de Bhaskara 10/04/2020
import math    # função matematica
a, b, c = map(float, input().split())
delta = b**2 - 4 * a * c       # formula delta
if delta < 0 or a == 0:    # condição para que exista as raizes
    print('Impossivel calcular')
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)   # formula para calcular a raiz x1
    print('R1 = {:.5f}'.format(raiz1))
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)  # formula para calcular a raix x2
    print('R2 = {:.5f}'.format(raiz2))
