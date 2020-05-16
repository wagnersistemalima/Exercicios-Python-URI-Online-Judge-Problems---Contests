# ex1113 Crescente e Decrescente For
while True:
    x, y = map(int, input().split())
    if x > y:
        print('Decrescente')
    elif x < y:
        print('Crescente')
    if x == y:
        break