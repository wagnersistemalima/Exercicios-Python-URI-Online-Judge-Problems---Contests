#Ex 1015  Distância entre dois pontos 09/04/2020
import math
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print('{:.4f}'.format(distancia))