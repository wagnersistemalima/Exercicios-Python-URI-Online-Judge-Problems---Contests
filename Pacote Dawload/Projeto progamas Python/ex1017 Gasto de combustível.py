#ex1017 Gasto de combustível 09/04/2020
tempo_gasto = int(input())
velocidade_media = int(input())
automovel = 12
distancia_percorrida = tempo_gasto * velocidade_media / automovel
print('{:.3f}'.format(distancia_percorrida))