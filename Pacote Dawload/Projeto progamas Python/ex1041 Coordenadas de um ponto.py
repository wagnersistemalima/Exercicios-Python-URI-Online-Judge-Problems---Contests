#Ex 1041 Coordenadas de um ponto 10/04/2020
x, y = map(float, input().split())
if x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
if x > 0 and y < 0:
    print('Q4')
elif x < 0 and y < 0:
    print('Q3')
elif x == 0 and y == 0:
    print('Origem')


