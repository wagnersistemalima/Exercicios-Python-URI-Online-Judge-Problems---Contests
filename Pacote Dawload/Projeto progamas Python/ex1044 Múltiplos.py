#1044  Múltiplos 10/04/2020
a, b = map(int, input().split())
if a % b == 0 or b % a == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')

