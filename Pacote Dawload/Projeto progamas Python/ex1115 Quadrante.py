#Ex 1115 Quadrante
partida = 0
while partida != 1:
    y, x = map(int, input().split())
    if y > 0 and x > 0:
        print('primeiro')
    elif y < 0 and x > 0:
        print('segundo')
    if y < 0 and x < 0:
        print('terceiro')
    elif y > 0 and x < 0:
        print('quarto')
    if y == 0 or x == 0:
        partida = partida + 1









