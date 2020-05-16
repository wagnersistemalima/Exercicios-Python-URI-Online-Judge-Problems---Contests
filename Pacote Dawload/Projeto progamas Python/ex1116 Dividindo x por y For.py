# ex1116 Dividindo x por y
n = int(input())

for c in range(1, n + 1):
    x, y = map(float, input().split())
    if x > y and y != 0:
        divisao = x / y
        print('{:.1f}'.format(divisao))
    elif x > y and y == 0:
        print('divisao impossivel')
    if x < y and y != 0:
        divisao = x / y
        print('{:.1f}'.format(divisao))
    elif x == y and y != 0:
        divisao = x / y
        print('{:.1f}'.format(divisao))
    if x < y and y == 0:
        print('divisao impossivel')






